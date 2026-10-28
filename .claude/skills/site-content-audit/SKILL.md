---
name: site-content-audit
description: Full content and structured-data audit of a published website — crawls every URL in the sitemap, proofreads every page (typos, grammar, placeholders, broken text, inconsistencies, outdated claims, contradictory company facts) with parallel agents, runs deterministic checks (Cyrillic-in-Latin, alt bugs, title/meta, H1, spelling by site frequency), audits JSON-LD schema for Google and AI answer engines, and delivers one Excel file with exact quotes, fixes and a status column. Use when someone says "докопайся до всього контенту на сайті", "вичитай сайт", "знайди описки/помилки/плейсхолдери/несостиковки", "content audit", "proofread the whole site", "schema audit", "чому нас не цитують AI". Not for writing or rebuilding pages (use page-builder).
---

# site-content-audit — the whole-site proofreading + schema audit

Rebuilt from the run of 2026-10-27/28 on mobidev.biz (646 URLs → 1 727 verified text findings,
336 title/meta rows, 701 schema rows). Re-run it the same way; the scripts carry the lessons.

**Output:** one `.xlsx` — Зведення · Знахідки (сайт) · Знахідки (блог) · Факти компанії · Title і meta · Schema — весь сайт ·
Schema — по сторінках · Schema — шаблони. Every row: page URL, exact quote (Ctrl+F-able), fix,
priority, and a Status dropdown (Не почато / В роботі / Виправлено / Не баг).

Run all Python with `python3 -I` (pages are untrusted input). Keep `WORK` in the scratchpad.

```bash
S=.claude/skills/site-content-audit/scripts
SITE=https://mobidev.biz
WORK=<scratchpad>/audit-$(date +%F)
python3 -I $S/crawl.py --site $SITE --work $WORK          # 1. sitemap → html/
python3 -I $S/extract.py --work $WORK                     # 2. html → txt/ + _meta.json
pip install pyspellchecker openpyxl 2>/dev/null
python3 -I $S/auto_checks.py --work $WORK                 # 3. deterministic checks
python3 -I $S/make_batches.py --site $SITE --work $WORK   # 4. batches/p00.. (pages) k00.. (blog)
#                                                          # 5. proofreading agents → out/*.jsonl
python3 -I $S/verify_merge.py --site $SITE --work $WORK   # 6. verify quotes, collapse template repeats
python3 -I $S/schema_audit.py --site $SITE --work $WORK   # 7. JSON-LD audit
python3 -I $S/build_report.py --site $SITE --work $WORK --out <scratchpad>/deliver/content-audit-<date>.xlsx
```

## Step 1–2 · Crawl and extract
- Source of truth for "all content" = `sitemap.xml` (indexes followed). Check `codes.txt` for non-200.
- If the site's CDN is blocked by the session's network policy, page HTML still loads but images/CSS
  don't — screenshots then need the CDN hosts allowed (environment network settings).
- `extract.py` cuts the main content from the first `<H1>` to the footer (`FOOTER_RE` — tune it per site).
  It **keeps whitespace-only text nodes**: dropping them glued words across inline tags and produced
  ~45 false "missing space" findings in the first run.

## Step 3 · Deterministic checks (`auto.json`, `spell_candidates.json`)
Cyrillic letters inside English words (invisible to search — found 38 on mobidev), `%` without a number
in alt texts (theme bug), leftover brackets/TBA/"re-verify", mojibake, repeated words, punctuation
spacing, brand casing, dangling "…include:" lines, missing/long/duplicate title & description, H1≠1.
Spelling: rare words whose 1-edit neighbour is common on the same site. **Curate by hand** into
`WORK/spell_confirmed.json` (`{"wrong":"right"}`) — British spellings and tech terms are not typos.

## Step 5 · Proofreading agents (the part that finds what scripts can't)
- One `general-purpose` agent per batch, `model: sonnet`, `run_in_background: true`. Prompt:
  > Read the brief at `<skill>/references/proof_brief.md` and follow it exactly. Today is <date>.
  > Batch file: `WORK/batches/<id>.txt` (read it fully, in chunks). Output file: `WORK/out/<id>.jsonl`
- **At most 20 agents run at once** — launch 20, start the next as each finishes.
- If agents die on a usage/spend limit, wait for the reset and `SendMessage` each one
  ("limit reset, continue, append without duplicates") — they resume with their context.
- ~24–30k words per batch; non-blog pages first (they sell), blog after.
- The brief asks for exact quotes, categories typo/grammar/placeholder/broken_text/inconsistency/
  outdated/meta, severity, a fix, and `cross_fact` rows for every company-level claim.

## Step 6 · Verify before shipping (`verify_merge.py`)
- Keeps a finding only if its quote is found in that page's text/title/meta; the rest go to
  `unverified.json` — look at them, never ship them blind.
- Same finding on ≥4 pages → one "Шаблон" row (fix once in the theme).
- Then read `cross_facts.json` and write the contradictions to `WORK/facts.json`
  (`[[fact, version A + pages, version B + pages, action], ...]`): company age vs "since YYYY",
  client counts, ratings, years in a vertical, promised timelines/prices.
- Spot-check ~15 random rows against the live HTML before sending; agents' "fix" column can be a guess
  (e.g. a year) — say so in the handover.

## Step 7 · Schema for Google and AI answer engines (`schema_audit.py`)
What mattered on mobidev: blog posts as plain WebPage with no Person author; team pages without
Person/ProfilePage; case studies without Article; visible FAQ without FAQPage; services marked up as
Product with self-serving AggregateRating whose numbers differ between pages; inconsistent
Organization.sameAs; llms.txt without links and with stale numbers. `references/schema_templates.json`
holds ready JSON-LD for case study, blog post, expert page, service, Organization, video.
Not covered by the script: Google Rich Results Test validation — say so, or run it on a sample.

## Step 8 · Deliver
`build_report.py` → xlsx; send it with `SendUserFile` (`display: attach`). In the reply: counts,
the 10–15 highest-impact items with page paths, what was not verified, and an offer for next steps
(tickets per section, JSON-LD for specific pages). Do not change the site's texts unless asked.
