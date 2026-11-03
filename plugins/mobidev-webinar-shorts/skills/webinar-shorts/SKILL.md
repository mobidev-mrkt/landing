---
name: webinar-shorts
description: Turn a MobiDev webinar recording (a Google Drive link to a Zoom recording) into 10 vertical YouTube Shorts, 20–60 s each, in the MobiDev brand, with a CTA end card, titles, descriptions and Google Drive folders. Use when someone sends a webinar video link and asks for Shorts, Reels, clips or "нарізку" from it, or says "зроби шортси з вебінару", "ось новий вебінар". Needs the it-reelsmaker plugin enabled; this skill fixes the decisions that worked on Webinar 13 so the next webinars go the same way.
---

# Webinar → 10 YouTube Shorts (MobiDev)

The method from Webinar 13 (Oct 2026): 10 Shorts in ~2.5 h of work. The **it-reelsmaker** plugin does the editing;
this skill pins every choice that was already made, so don't ask about them again: brand `mobidev`, style "Brand",
subtitles "Accent", English, "framed" layout, natural pacing ×1.1, designed scenes only (no B-roll, memes, music),
logo only on the end card, voice only (music is picked in YouTube), 5 + 5 CTAs.

Talk to the person in their language (Ukrainian so far). Load the it-reelsmaker skill too (`Skill: it-reelsmaker:it-reelsmaker`)
for its rules (quality rules, reading-time floor, facts only from the speech); this file overrides its questions.

## What to ask, and only this
From the request take: the video link, the CTA split (default: 5 × `discovery`, 5 × `checklist` from
`reels/brands/mobidev/cta.md`), anything new. Two stops for approval, both required:
1. **10 moments** with webinar timecodes, speaker, hook line, CTA (step 3).
2. **Hooks and scene texts** for all 10 (step 7). A cut plan is shown together with the moments' approval only if
   something unusual came up (retakes, cut-out words).
Then render without further questions and deliver.

## Files and ids
`$W` = this skill's `scripts/` folder (the "Base directory for this skill" shown when it loads, plus `/scripts`).
The working project is `reels/` at the root of the current git repo (created by `setup.sh` with the MobiDev brand
from this plugin's `assets/` if it is missing; an existing `reels/` with its brand is kept). The Remotion project
goes next to it, `reels-remotion/`, and is kept out of git.
Webinar id `w<N>` (for example `w14`), video ids `w14-01` … `w14-10`. Everything lives in `reels/`:
`source/w14.mov` (not in git), `edit/w14-clips.tsv`, `edit/w14-spans.tsv`, `edit/w14-hooks.tsv`, `edit/w14-scenes.sh`,
`edit/w14-01/…`, deliveries in `edit/delivery/w14/<cta key>/`. `source $W/env.sh` sets `$S` (the it-reelsmaker
scripts), `$REELS`, `$R` and `$B`.

## Steps

**0. Setup** (fresh container, ~5 min): `bash $W/setup.sh`, then `source $W/env.sh`. It creates `reels/` if needed
(MobiDev brand, settings, `.gitignore`), installs gdown, faster-whisper (medium), opencv, the YuNet face model, the
Remotion project `reels-remotion/` (outside git) with the kit override from `assets/`, and exports the brand.
Work on the session's branch; commit and push the project files (not video) as you go.

**1. Download** with gdown by file id (this gdown has no `--fuzzy`):
`cd reels/source && gdown <FILE_ID> -O w14.mov`. Probe it (`ffprobe`): expect 1920×1080 Zoom, ~60 min.

**2. Scouting transcript** of the whole hour (~15 min, run in the background):
`ffmpeg -i source/w14.mov -vn -ac 1 -ar 16000 edit/_scout/w14.wav` then
`python3 $W/scout.py edit/_scout/w14.wav edit/_scout/w14`. Meanwhile grab frames every 5 min
(`fps=1/300,scale=480:270,tile=4x3`) and check the speaker window: MobiDev's Zoom template puts it at
x 192–1728, y 183–1046 with the name plate bottom-left from y ≈ 895. If the frames differ, measure a full-size frame
and pass `CROP=w:h:x:y` (above the name plate) to `make_clips.sh`.

**3. Pick 10 moments** (read the whole transcript): a self-contained thought, story or number, 30–70 s of raw speech
→ 25–55 s after the cut. Prefer stories with a payoff (a client case, a failure, a paradox), lists ("three questions",
"four steps") and numbers; skip the host's lines, intros, Q&A logistics, the slides at the end. Split the CTA by topic:
process / AI SDLC adoption → `discovery`; legacy / modernization → `checklist`. Mix the speakers.
Show a table: # · webinar timecode · speaker · hook line · CTA, plus 2–3 reserves. **Wait for "yes".**

**4. Clips and transcripts.** Write `edit/w14-clips.tsv` (`id<TAB>start<TAB>end<TAB>SPEAKER NAME`, source seconds with
3–5 s of margin; extend a clip if the thought ends after it) and run `bash $W/make_clips.sh w14`. Each clip is the crop
plus a #222222 strip below (subtitles live there; without it the chin sits at the crop's bottom edge and there is no
room for subtitles). Transcripts: medium, ~0.6× real time.

**5. Cut lists.** Read each transcript (`python3 $W/words.py src w14-01`, words in a range: `… src w14-01 12-15`) and
choose spans by meaning: whole sentences, drop the host, false starts, "you know it's like with this thing",
unclear phrases. **Span edges go in the middle of the pauses**, never at Whisper's word start/end (they fall inside
the sound). Re-transcribe doubtful spots without context: `python3 $S/transcribe.py snip edit/<id> source/<id>.mp4
--from A --to B` (≤ 5 s): it finds "um" at an edge and self-corrections ("depends, um, depended": no pause → keep
whole, fix the subtitle). Write `edit/w14-spans.tsv` (`id<TAB>a-b,c-d,…`) and run `python3 $W/build_cuts.py w14`.
It uses `--thr -38` (Zoom audio is quiet; −30 dropped real words), natural pacing, speed 1.1, merges ranges where a
word fell into a cut pause, measures white balance, builds and checks every edge by audio. For each remaining edge
warning: snip-transcribe it, move the edge, rebuild with `python3 $W/build_cuts.py w14 w14-03`.
Fix recognition errors in `cut.json → fix` (every occurrence) or `fix_at` (`at` = source second of the word): names
(Serhii, Ievgen, MobiDev), "QA" heard as "key", "spec" as "space", "SDLC" as "DLC"/"AIS DLC", "repo" as "wrapper".
Then `cut.py edit/<id>` again (build_cuts keeps your fixes).

**6. Layout and faces:** `bash $W/setup_videos.sh w14` (framed window `[25,600,1030,900]`, no label, Brand/Accent,
calm). It prints spans without room for subtitles: should be 0.

**7. Hooks and scenes.** Hooks in `edit/w14-hooks.tsv` (`id<TAB>hook<TAB>cta key`): ≤ 28 characters so it breaks into
2 lines of ≤ 14 (longer → 4 lines over the face); a fact or a question from the clip, no hype. Scenes: copy
`$W/scenes.template.sh` to `edit/w14-scenes.sh` (run it with `WEBINAR_SHORTS_ENV=$W/env.sh`), 1–2 per video (quote, list, stat), anchored on spoken words
(`python3 $W/words.py out w14-01`), all `--mode overlay --box 60,240,900,340` (the field above the window). Run it,
then `python3 $S/visual_plan.py validate edit/<id> --card` until 0 errors: fix reading-time errors by starting the
scene earlier or making it longer; a quote must be a verbatim run of the transcript; if a scene must outlast the
cut's end, extend the last range by 0.1–0.3 s of silence. Show all hooks and scene texts plus the two CTA lines in
one table. **Wait for "yes".**

**8. Render all:** `bash $W/render.sh w14` in the background (~1.5–2 min per video). Each line ends with LUFS, peak and
the face audit. "Face in the subtitle band" while the speaker leans forward is expected here: the text sits on the dark
strip below the picture; confirm on a frame (`ffmpeg -ss T -i <mp4> -frames:v 1 …`) instead of re-rendering.
Then contact sheets (8 frames per video, `fps=8/<dur>,scale=135:240,tile=8x1`) and look at them: hook in 2 lines,
lists readable, end card. Send the MP4s with SendUserFile (two batches: discovery, checklist).

**9. Descriptions and Drive.** Per video: title (≤ 70 chars + `#Shorts`), 1–3 sentences in the brand voice with the
speaker's name and role, the CTA line with `[LINK]`, 3–4 hashtags; claims only from the speech; no emoji (Drive's
markdown import breaks them; use "→"). Save `edit/w14-descriptions.md`. On Google Drive: a folder
"MobiDev Webinar <N> — YouTube Shorts" with two subfolders, "Offer — Free AI SDLC Readiness Discovery" and
"Checklist — AI-Driven Modernization Readiness", each with a Google Doc of its descriptions (`create_file`,
`contentMimeType: text/markdown`). **The MP4s cannot go through the Drive connector** (it takes the file inline as
base64; 8–18 MB per video is too large): say so and give the folder links for a manual drag-and-drop.

**10. Time log and commit.** Write `edit/w14-time-log.md` from commit times (stage · from · to · minutes; work vs
waiting for approvals) and report the total. Commit everything except video, audio, clips and logs (`reels/.gitignore`
covers them) and push.

## Environment workarounds (all already in the scripts)
- faster-whisper on a file path fails (`metadata_errors`): feed a numpy array (`scout.py`); `transcribe.py` works.
- Remotion can't download its browser: render with `--browser-executable=$B` (Playwright's headless shell).
- The browser does not trust the proxy CA, so Google Fonts fail: the brand uses local woff2 files
  (`reels/brands/mobidev/assets/fonts/`, `source: local`). Don't switch back to `google`.
- The kit shrinks the 60-character checklist CTA to ~30 px: `assets/remotion-overrides/ReelKit.tsx` wraps it into
  2–3 lines; `setup.sh` copies it over the kit (run it again after any `kit.py update`).
- `poster.py bake` (cover in frame 0) is skipped: re-encoding the soft footage fails its own quality check.
- The YuNet model from github.com/raw is an LFS pointer; `setup.sh` downloads from media.githubusercontent.com.

## Numbers from Webinar 13 to compare against
10 videos 27.5–58.0 s (incl. 2.6 s end card), −14.0…−14.3 LUFS, true peak ≤ −1.3 dBFS, 0 text-on-face overlaps;
about 3 h end to end (2 h 35 min of work, the rest waiting for approvals). Its working files are in the
`mobidev-mrkt/landing` repo under `reels/edit/` (cut plan, descriptions, time log, scenes, hooks).
