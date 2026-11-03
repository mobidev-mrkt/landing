#!/bin/bash
# Working clips + word-level transcripts for one webinar.
# usage: bash make_clips.sh <w>    reads reels/edit/<w>-clips.tsv: id<TAB>start_s<TAB>end_s<TAB>speaker
#   (source seconds, 3–5 s of margin on both sides; id like w14-01)
# Each clip: the Zoom speaker window cropped above the MobiDev nameplate, then a #222222 strip padded below
# (subtitles sit there, under the chin). CROP=w:h:x:y overrides the window (MobiDev Zoom layout: 1536:710:192:183).
source "$(dirname "$0")/env.sh"; cd "$REELS" || exit 1
w=$1; CROP=${CROP:-1536:710:192:183}; SRC=${SRC:-source/$w.mov}
cw=${CROP%%:*}; rest=${CROP#*:}; ch=${rest%%:*}; ph=$(( (ch * 5 / 4 + 1) / 2 * 2 ))   # strip = 25% of the crop height
while IFS=$'\t' read -r id a b who; do
  [ -z "$id" ] && continue
  ffmpeg -v error -ss "$a" -to "$b" -i "$SRC" -vf "crop=$CROP,pad=$cw:$ph:0:0:color=0x222222" -r 30 \
    -c:v libx264 -crf 17 -preset fast -pix_fmt yuv420p -c:a aac -b:a 192k -y "source/$id.mp4" &
done < "edit/$w-clips.tsv"; wait
while IFS=$'\t' read -r id a b who; do
  [ -z "$id" ] && continue
  mkdir -p "edit/$id"
  python3 "$S/transcribe.py" "edit/$id" "source/$id.mp4" --model medium --language en 2>&1 | grep -E "^!|words"
done < "edit/$w-clips.tsv"
