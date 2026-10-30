#!/bin/bash
# Render, check and master the Shorts of one webinar.
# usage: bash render.sh <w> [id ...]    reads reels/edit/<w>-hooks.tsv: id<TAB>hook (≤ 2 lines of ≤ 14 chars)<TAB>cta key
# cta key = a "## key" section of brands/mobidev/cta.md (Main → card line 1, Clarifier → line 2).
# Steps: export props → hook stays until the first scene → render (local headless Chromium) → face audit
# → cover pick → master −14 LUFS → cover art → reels/edit/delivery/<w>/<cta key>/<id>.mp4
# Frame-0 cover bake is skipped on purpose: re-encoding soft Zoom footage costs quality (PSNR 28 dB).
source "$(dirname "$0")/env.sh"; cd "$REELS" || exit 1
w=$1; shift
cta(){ awk -v k="## $1" -v f="$2" '$0==k{on=1;next} /^## /{on=0} on && $0 ~ "^- "f": "{sub("^- "f": ","");print;exit}' brands/mobidev/cta.md; }
while IFS=$'\t' read -r id hook key; do
  [ -z "$id" ] && continue
  [ $# -gt 0 ] && [[ ! " $* " =~ " $id " ]] && continue
  E=edit/$id; P=$(pwd)/$E/reelkit-props.json; O=$R/out/$id; D=edit/delivery/$w/$key
  L1=$(cta "$key" Main); L2=$(cta "$key" Clarifier)
  [ -z "$L1" ] && { echo "$id: no CTA '$key' in cta.md"; continue; }
  python3 "$S/visual_plan.py" validate "$E" --card > "$E/validate.log" 2>&1 || { echo "$id: plan errors"; grep -E '^error' "$E/validate.log"; continue; }
  python3 "$S/visual_plan.py" export "$E" --remotion "$R" --props "$P" --subtitles accent --hook "$hook" --card "$L1" "$L2" > "$E/export.log" 2>&1 || { echo "$id export FAIL"; continue; }
  python3 - "$P" <<'PY'
import json, sys
p = sys.argv[1]; d = json.load(open(p)); first = min([s["start"] for s in d.get("scenes", [])] or [99])
d["hook"]["until"] = round(max(2.4, first - 0.1), 2); json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
PY
  mkdir -p "$R/out"
  (cd "$R" && npx remotion render ReelKit "$O.mp4" --props="$P" --browser-executable="$B" --concurrency=4 > "$O.render.log" 2>&1)
  { [ $? -eq 0 ] && [ "$O.mp4" -nt "$P" ]; } || { echo "$id render FAIL"; tail -5 "$O.render.log"; continue; }
  python3 "$S/faces.py" audit "$O.mp4" --edit "$E" > "$E/audit.log" 2>&1
  python3 "$S/poster.py" pick "$E" --render "$O.mp4" -o "$E/cover.jpg" > "$E/poster.log" 2>&1
  python3 "$S/master_audio.py" "$O.mp4" -o "$O-master.mp4" > "$E/master.log" 2>&1 || { echo "$id master FAIL"; tail -4 "$E/master.log"; continue; }
  mkdir -p "$D"; python3 "$S/poster.py" attach "$O-master.mp4" --cover "$E/cover.jpg" -o "$D/$id.mp4" >> "$E/poster.log" 2>&1
  echo "$id DONE → $D/$id.mp4 | $(grep -E '^output' "$E/master.log") | audit: $(grep -E '✗|no overlaps' "$E/audit.log" | head -1 | cut -c1-110)"
done < "edit/$w-hooks.tsv"
