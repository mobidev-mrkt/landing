"""Fast scouting transcript of a whole webinar (small.en, ~4x real time on 4 CPUs) with [mm:ss] per line.
usage: python3 scout.py <audio16k.wav> <out-prefix>   → <out-prefix>.txt, <out-prefix>.json
The audio is fed as a numpy array: the installed PyAV rejects faster-whisper's own file opening."""
import json, sys, wave
import numpy as np
from faster_whisper import WhisperModel

w = wave.open(sys.argv[1])
a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
m = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=4)
segs, _ = m.transcribe(a, language="en", vad_filter=True, beam_size=1)
out = []
with open(sys.argv[2] + ".txt", "w") as f:
    for s in segs:
        out.append({"start": s.start, "end": s.end, "text": s.text})
        t = int(s.start)
        f.write(f"[{t // 60:02d}:{t % 60:02d}] {s.text.strip()}\n"); f.flush()
json.dump(out, open(sys.argv[2] + ".json", "w"))
