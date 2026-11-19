#!/usr/bin/env python3
"""MobiDev brand patches to the Remotion kit in <remotion dir>/src/kit (run by setup.sh; safe to run again).

1. contrast: the strike-through over the "before" line is drawn in colors.extra.problem (#DE7356, the Brand Book's
   coral for a problem or a mistake) instead of the accent green.
Each patch is a literal replacement; if the kit changed and the text is not found, it says so and leaves the file.
usage: python3 patch_kit.py <remotion dir>
"""
import pathlib, sys

R = pathlib.Path(sys.argv[1]) / "src" / "kit" / "scenes"
PATCHES = [
    ("Contrast.tsx",
     "backgroundColor: plates ? card.text : surf.accent }}",
     "backgroundColor: c.brand.colors.extra?.problem ?? (plates ? card.text : surf.accent) }} /* mobidev: coral strike */"),
]
for name, old, new in PATCHES:
    p = R / name
    if not p.exists():
        print(f"kit patch: {p} not found, skipped"); continue
    s = p.read_text()
    if new in s:
        print(f"kit patch: {name} already patched"); continue
    if s.count(old) != 1:
        print(f"!! kit patch: {name}: pattern not found (kit changed?), left as is"); continue
    p.write_text(s.replace(old, new)); print(f"kit patch: {name} patched")
