#!/bin/bash
# One-time setup of a fresh cloud container (≈5 min). Safe to run again.
# Creates the working project reels/ (MobiDev brand, settings, .gitignore) if it is missing, installs Python packages,
# Whisper medium and the face model, the Remotion project with the kit + local override, and exports the brand.
source "$(dirname "$0")/env.sh"
mkdir -p "$REELS/brands" "$REELS/source" "$REELS/edit" "$REELS/models"; cd "$REELS" || exit 1
[ -f brands/mobidev/brand.json ] || { cp -r "$A/brand-mobidev" brands/mobidev && echo "brand: MobiDev copied into reels/brands/mobidev"; }
[ -f .gitignore ] || cp "$A/reels.gitignore" .gitignore
[ -f it-reelsmaker.json ] || printf '{\n  "project_root": ".",\n  "remotion_dir": "../reels-remotion",\n  "face_model": "models/face_detection_yunet_2023mar.onnx"\n}\n' > it-reelsmaker.json
grep -q '^models/' .gitignore || echo "models/" >> .gitignore
pip install -q gdown faster-whisper opencv-python-headless 2>&1 | grep -v WARNING
python3 -c "from faster_whisper import download_model; download_model('medium')" >/dev/null 2>&1 && echo "whisper medium: ok"
if [ "$(stat -c%s models/face_detection_yunet_2023mar.onnx 2>/dev/null)" != "232589" ]; then
  # github.com/raw returns an LFS pointer here; media.githubusercontent.com serves the real file
  curl -sSL -o models/face_detection_yunet_2023mar.onnx \
    "https://media.githubusercontent.com/media/opencv/opencv_zoo/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"
fi
echo "face model: $(stat -c%s models/face_detection_yunet_2023mar.onnx) bytes (expect 232589)"
if [ ! -d "$R/node_modules" ]; then
  [ -d "$R" ] || python3 "$S/kit.py" new "$R"
  (cd "$R" && npm install >/dev/null 2>&1) && echo "remotion: installed"
fi
cp "$A/remotion-overrides/ReelKit.tsx" "$R/src/ReelKit.tsx" && echo "kit override: applied (long CTA wraps)"
# keep the Remotion project (node_modules) out of git
top=$(git rev-parse --show-toplevel 2>/dev/null) && { grep -qx 'reels-remotion/' "$top/.git/info/exclude" 2>/dev/null || echo "reels-remotion/" >> "$top/.git/info/exclude"; }
python3 "$S/brand.py" export mobidev --remotion "$R" | tail -1
python3 "$S/doctor.py" --remotion "$R" | tail -3
