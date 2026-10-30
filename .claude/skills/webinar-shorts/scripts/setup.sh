#!/bin/bash
# One-time setup of a fresh cloud container (≈5 min): Python packages, Whisper medium, face model,
# Remotion project with the kit + local override, brand export. Safe to run again.
source "$(dirname "$0")/env.sh"; cd "$REELS" || exit 1
pip install -q gdown faster-whisper opencv-python-headless 2>&1 | grep -v WARNING
python3 -c "from faster_whisper import download_model; download_model('medium')" >/dev/null 2>&1 && echo "whisper medium: ok"
mkdir -p models
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
cp remotion-overrides/ReelKit.tsx "$R/src/ReelKit.tsx" && echo "kit override: applied (long CTA wraps)"
grep -q '^\.\./reels-remotion\|^reels-remotion/' ../.git/info/exclude 2>/dev/null || echo "reels-remotion/" >> ../.git/info/exclude
python3 "$S/brand.py" export mobidev --remotion "$R" | tail -1
python3 "$S/doctor.py" --remotion "$R" | tail -3
