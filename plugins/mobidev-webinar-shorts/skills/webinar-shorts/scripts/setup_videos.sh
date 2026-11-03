#!/bin/bash
# Video settings, face measurement and empty visual plans for every clip of one webinar.
# usage: bash setup_videos.sh <w>     (after build_cuts.py)
# Layout: "framed", window [25,600,1030,900], no label (the field above the window holds the hook, then the scenes),
# style Brand, subtitles Accent, scene tone calm, only designed scenes as inserts.
source "$(dirname "$0")/env.sh"; cd "$REELS" || exit 1
w=$1
while IFS=$'\t' read -r id a b who; do
  [ -z "$id" ] && continue
  python3 "$S/brand.py" use mobidev --edit "edit/$id" >/dev/null 2>&1
  python3 "$S/reelcfg.py" save "edit/$id" --set style=brand subtitles=accent scene_tone=calm format=framed \
    use_broll=false use_scenes=true use_memes=false use_generated_footage=false >/dev/null
  python3 - "edit/$id/reel.json" "$who" <<'PY'
import json, sys
p = sys.argv[1]; d = json.load(open(p)); d.pop("label", None); d["speaker"] = sys.argv[2]; d["window"] = [25, 600, 1030, 900]
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
PY
  python3 "$S/faces.py" scan "edit/$id" >/dev/null 2>&1
  python3 "$S/visual_plan.py" init "edit/$id" >/dev/null 2>&1
  echo "$id: spans without room for subtitles: $(python3 "$S/faces.py" zones "edit/$id" 2>&1 | grep -E '^k' | grep -c 'no room')"
done < "edit/$w-clips.tsv"
