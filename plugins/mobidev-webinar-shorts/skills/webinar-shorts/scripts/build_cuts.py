"""Rough cuts for one webinar: audio edges → cut.json → no dropped words → white balance → cut.py → edge check.
usage: python3 build_cuts.py <w> [id ...]     reads reels/edit/<w>-spans.tsv: id<TAB>spans (clip seconds, a-b,c-d)
Spans start and end in the MIDDLE of pauses, not at Whisper's word edges (those land inside the sound).
Defaults that worked on Zoom audio: --thr -38 (−30 drops quiet words), natural pacing, speed 1.1.
Existing "fix"/"fix_at" in cut.json are kept. Run from anywhere."""
import json, os, re, subprocess, sys

env = dict(os.environ)
S, REELS = env["S"], env["REELS"]
os.chdir(REELS)
run = lambda *a: subprocess.run(["python3", *a], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True).stdout

w = sys.argv[1]
only = set(sys.argv[2:])
for line in open(f"edit/{w}-spans.tsv"):
    if not line.strip(): continue
    id, spans = line.rstrip("\n").split("\t")[:2]
    if only and id not in only: continue
    out = run(f"{S}/speech_mask.py", f"edit/{id}/audio16k-{id}.wav", "--spans", spans, "--thr", "-38", "--density", "natural")
    rs = json.loads(re.search(r'"ranges": (\[.*?\])', out, re.S).group(1))
    for r in rs: r.pop("beat", None)
    p = f"edit/{id}/cut.json"
    old = json.load(open(p)) if os.path.exists(p) else {}
    cj = {"fps": 30, "speed": 1.1, "scale": "auto",
          "sources": {"main": {"file": f"source/{id}.mp4", "transcript": f"edit/{id}/transcripts/{id}.json"}},
          "ranges": rs}
    for k in ("fix", "fix_at", "look"):
        if k in old: cj[k] = old[k]
    json.dump(cj, open(p, "w"), indent=1)
    # a transcript word in a removed gap = a quiet word under the threshold (or Whisper drift): keep the pause instead
    for _ in range(20):
        dry = run(f"{S}/cut.py", f"edit/{id}", "--dry-run")
        gaps = re.findall(r"falls in the ([0-9.]+)-([0-9.]+) gap", dry)
        if not gaps: break
        a, b = map(float, gaps[0]); cj = json.load(open(p)); rs = cj["ranges"]
        for i in range(len(rs) - 1):
            if abs(rs[i]["end"] - a) < 0.05 and abs(rs[i + 1]["start"] - b) < 0.05:
                rs[i]["end"] = rs[i + 1]["end"]; del rs[i + 1]; break
        else: break
        json.dump(cj, open(p, "w"), indent=1)
    cj = json.load(open(p)); cj["ranges"] = [r for r in cj["ranges"] if r["end"] > r["start"] + 0.05]; json.dump(cj, open(p, "w"), indent=1)
    if "look" not in old: run(f"{S}/balance.py", f"edit/{id}", "--write")
    built = run(f"{S}/cut.py", f"edit/{id}")
    m = re.search(r"ready: ([0-9.]+) s", built)
    edges = run(f"{S}/speech_mask.py", "--edl", f"edit/{id}/edl.json")
    warns = [l.strip() for l in edges.splitlines() if "⚠" in l]
    print(f"{id}: {m.group(1) if m else 'CUT FAILED'} s, {len(cj['ranges'])} ranges, edge warnings {len(warns)}")
    for l in warns: print("   ", l[:160])
    if not m: print(built[-600:])
