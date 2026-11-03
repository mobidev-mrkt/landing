#!/bin/bash
# Render pipeline for one Short: export props → render → face audit → cover pick → master → cover art.
# Frame-0 bake is skipped: re-encoding the soft Zoom footage costs quality (frame PSNR 28 dB).
# usage: bash edit/render.sh 09   (run from reels/)
set -u
id=$1
S=/root/.claude/plugins/synced/c347354c-4cb9-45b3-b39b-0ac1576e85d9_7e769f59-ffb2-4b04-a2ff-96c3350fa29f/c1ae3d1a-cbd2-4ee3-be95-a87be163ba1f/skills/it-reelsmaker/scripts
B=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell
R=$(cd ../reels-remotion && pwd); E=edit/short$id; P=$(pwd)/$E/reelkit-props.json; O=$R/out/short$id
hook=$(awk -F'\t' -v i=$id '$1==i{print $2}' edit/hooks.tsv)
if [ "$id" -le 05 ]; then L1="Free AI SDLC Readiness Discovery"; L2="Book yours — link in description";
else L1="Download the free AI-Driven Modernization Readiness Checklist"; L2="Link in description"; fi
python3 $S/visual_plan.py export $E --remotion $R --props $P --subtitles accent --hook "$hook" --card "$L1" "$L2" > $E/export.log 2>&1 || { echo "$id export FAIL"; exit 1; }
python3 - "$P" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p)); first=min([s["start"] for s in d.get("scenes",[])] or [99])
d["hook"]["until"]=round(max(2.4,first-0.1),2); json.dump(d,open(p,"w"),indent=1,ensure_ascii=False)
PY
(cd $R && npx remotion render ReelKit $O.mp4 --props=$P --browser-executable=$B --concurrency=4 > $O.render.log 2>&1); rc=$?
[ $rc -eq 0 ] && [ $O.mp4 -nt $P ] || { echo "$id render FAIL ($rc)"; tail -5 $O.render.log; exit 1; }
python3 $S/faces.py audit $O.mp4 --edit $E > $E/audit.log 2>&1; echo "$id audit: $(tail -1 $E/audit.log)"
python3 $S/poster.py pick $E --render $O.mp4 -o $E/cover.jpg > $E/poster.log 2>&1
python3 $S/master_audio.py $O.mp4 -o $O-master.mp4 > $E/master.log 2>&1 || { echo "$id master FAIL"; tail -5 $E/master.log; exit 1; }
mkdir -p edit/delivery
python3 $S/poster.py attach $O-master.mp4 --cover $E/cover.jpg -o edit/delivery/short$id.mp4 >> $E/poster.log 2>&1 || { echo "$id attach FAIL"; exit 1; }
echo "$id DONE $(tail -2 $E/master.log | tr '\n' ' ')"
