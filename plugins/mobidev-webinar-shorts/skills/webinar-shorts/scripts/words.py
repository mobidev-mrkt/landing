"""Print words with times, to pick cut edges and scene anchors.
  python3 words.py src <id> [from-to ...]   source transcript (clip seconds): lines with gaps, or words in ranges
  python3 words.py out <id> [<id> ...]      the rough cut's captions (output seconds), for scene --at anchors
run from reels/"""
import json, os, sys

def src(id, ranges):
    d = json.load(open(f"edit/{id}/transcripts/" + sorted(os.listdir(f"edit/{id}/transcripts"))[0]))
    ws = d["words"]
    t = lambda w: (w.get("word") or w.get("text")).strip()
    if ranges:
        for r in ranges:
            a, b = map(float, r.split("-"))
            print(f"[{r}] " + " ".join(f"{t(w)}@{w['start']:.2f}-{w['end']:.2f}" for w in ws if w["end"] > a and w["start"] < b))
        return
    line, ls, prev = [], None, None
    for w in ws:
        if prev is not None and (w["start"] - prev > 0.45 or len(line) >= 14):
            print(f"{ls:6.2f} | " + " ".join(line)); line, ls = [], None
            if w["start"] - prev > 0.45: print(f"        ~gap {w['start'] - prev:.2f}")
        ls = w["start"] if ls is None else ls
        line.append(t(w) + (f"[{w['end'] - w['start']:.1f}s]" if w["end"] - w["start"] > 1 else "")); prev = w["end"]
    if line: print(f"{ls:6.2f} | " + " ".join(line))

def out(ids):
    for id in ids:
        c = json.load(open(f"edit/{id}/captions.json"))
        print(f"== {id} dur {c.get('duration')}")
        ws = [f"{w['text']}@{w['start']:.1f}" for w in c["words"]]
        for i in range(0, len(ws), 12): print(" ".join(ws[i:i + 12]))

if sys.argv[1] == "src": src(sys.argv[2], sys.argv[3:])
else: out(sys.argv[2:])
