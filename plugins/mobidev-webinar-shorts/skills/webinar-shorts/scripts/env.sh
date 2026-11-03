#!/bin/bash
# Paths used by every webinar-shorts script. Source it: `source <skill dir>/scripts/env.sh`
# W: this skill's scripts; A: its assets (MobiDev brand, kit override); REELS: the working project, reels/ at the root
# of the current git repo (or of the current folder); S: it-reelsmaker plugin scripts; B: preinstalled headless
# Chromium (Remotion cannot download its own here); R: Remotion project next to reels/ (outside reels/).
export W=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export A=$(cd "$W/../assets" && pwd)
export REELS=${REELS:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)/reels}
export S=$(ls -d /root/.claude/plugins/synced/*/*/skills/it-reelsmaker/scripts 2>/dev/null | head -1)
[ -z "$S" ] && S=$(find / -path '*skills/it-reelsmaker/scripts/cut.py' -not -path '/proc/*' 2>/dev/null | head -1 | xargs -r dirname)
export B=$(ls /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)
export R=$(dirname "$REELS")/reels-remotion
[ -z "$S" ] && echo "!! it-reelsmaker plugin not found: enable it for this session" >&2
true
