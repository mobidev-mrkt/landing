#!/bin/bash
# Paths used by every webinar-shorts script. Source it: `source .claude/skills/webinar-shorts/scripts/env.sh`
# S: it-reelsmaker plugin scripts; B: preinstalled headless Chromium (Remotion cannot download its own here);
# R: Remotion project; W: this skill's scripts; REELS: project root (reels/).
export W=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export REELS=$(cd "$W/../../../../reels" && pwd)
export S=$(ls -d /root/.claude/plugins/synced/*/*/skills/it-reelsmaker/scripts 2>/dev/null | head -1)
[ -z "$S" ] && S=$(find / -path '*skills/it-reelsmaker/scripts/cut.py' 2>/dev/null | head -1 | xargs -r dirname)
export B=$(ls /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell 2>/dev/null | head -1)
export R=$(cd "$REELS/.." && pwd)/reels-remotion
[ -z "$S" ] && echo "!! it-reelsmaker plugin not found: enable it for this session" >&2
true
