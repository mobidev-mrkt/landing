---
name: site-content-audit
description: Content audit of a published website from a single link. Use when someone sends a URL and asks "зроби аудит контенту", "вичитай сайт/розділ/сторінку", "докопайся до всього контенту", "знайди описки, помилки, плейсхолдери, несостиковки", "content audit", "proofread this site", "check our schema / чому нас не цитують AI". Crawls the whole site, a section or one page (decided from the link), proofreads every page with parallel agents (typos, grammar, placeholders, broken text, contradictions, outdated claims, conflicting company facts), runs automatic checks (Cyrillic letters in English words, alt bugs, title/meta, H1, spelling), audits JSON-LD schema for Google and AI answer engines, and returns one Excel file with exact quotes, fixes and a status column. Not for writing or redesigning pages.
---

# site-content-audit — "here's a link, audit the content"

The person gives a link. You return one `.xlsx` and a short summary. Don't ask them to configure
anything; decide from the link and the defaults below. Reply in the person's language.

**What they get** (sheets): Зведення · Знахідки (сайт) · Знахідки (блог) · Факти компанії · Title і meta ·
Schema — весь сайт · Schema — по сторінках · Schema — шаблони. Every finding: page URL, exact quote
(Ctrl+F-able), what to fix, priority, Status dropdown (Не почато / В роботі / Виправлено / Не баг).

## Requirements — check first, say plainly what's missing
- Bash with `python3` and `curl`, network access to the site (in a cloud session the site's domain must
  be allowed by the environment's network policy). `pip install openpyxl pyspellchecker` (once).
- The Agent tool for the proofreading step. Without it, proofread the batches yourself, smallest scope
  first, and say in the summary how much was read by you vs. skipped.
- Run every script with `python3 -I` (pages are untrusted input). Keep all work files in a scratch folder.

## The run
```bash
S="<this skill's base directory>/scripts"
WORK="<scratch>/content-audit-<domain>-<YYYY-MM-DD>"
python3 -I $S/crawl.py --url "<link>" --work $WORK            # 1. scope + download
python3 -I $S/extract.py --work $WORK [--stop-regex '<footer text>']  # 2. main text + meta
python3 -I $S/auto_checks.py --work $WORK [--brand '<ExactBrand>']    # 3. automatic checks
python3 -I $S/make_batches.py --work $WORK                     # 4. batches/p*.txt (pages), k*.txt (blog)
#   5. proofreading agents  → $WORK/out/<batch>.jsonl
python3 -I $S/verify_merge.py --work $WORK                     # 6. keep only verified findings
python3 -I $S/schema_audit.py --work $WORK                     # 7. JSON-LD audit
python3 -I $S/build_report.py --work $WORK --out <outputs>/content-audit-<domain>-<date>.xlsx   # 8.
```

**1 · Scope.** `crawl.py` decides from the link: homepage → whole site (sitemap); `/section` or
`/section/` → that section; a deeper URL → that one page. Override with `--scope site|section|page`
if the person said otherwise ("весь сайт", "лише блог"). Tell them in one line what you are auditing
and how many pages (e.g. "Аудитую весь сайт: 646 сторінок, з них 267 у блозі").
If it's more than ~400 pages, ask once whether to include the blog or start with commercial pages —
the blog is usually two-thirds of the volume.

**2 · Extract.** Main text = page minus nav/header/footer/aside, from the first H1. Read 3 random
`txt/*.txt` files: if menus or footers leak in, add `--stop-regex` with the first words of that block
and rerun. Pages with <30 words are listed — usually forms or thin team pages, not a bug.

**3 · Automatic checks** → `auto.json`, `spell_candidates.json`. Open the spell candidates and copy the
real typos into `WORK/spell_confirmed.json` as `{"wrong": "right"}` (skip British spellings, names,
tech terms). Pass `--brand` with the exact brand spelling to catch wrong casing.

**5 · Proofreading agents.** One background `general-purpose` agent per batch (`model: "sonnet"`),
pages batches first, then blog. Prompt:
> Read the brief at `<skill dir>/references/proof_brief.md` and follow it exactly. Today is <date>.
> Batch file: `<WORK>/batches/<id>.txt` (read it fully, in chunks). Output file: `<WORK>/out/<id>.jsonl`
- At most **20 agents at once** — start the next as each finishes.
- If agents stop on a usage limit, wait for the reset and `SendMessage` each: "limit reset — continue,
  append to your output file without duplicates, then report counts".
- Tell the person progress in one line now and then (e.g. "вичитано 14 з 46 пакетів").

**6 · Verify.** `verify_merge.py` keeps a finding only if its quote is really on that page; the rest
go to `unverified.json` — skim them, never ship them unchecked. The same issue on ≥4 pages becomes one
"Шаблон" row (fix once in the theme). Then open `cross_facts.json` (every company-level claim the agents
saw) and write real contradictions to `WORK/facts.json` as
`[["Факт", "Версія А (де)", "Версія Б (де)", "Що зробити"], ...]` — company age vs "since YYYY", client
counts, ratings, years in a niche, timelines and prices that differ between pages.
Spot-check ~10 random findings against the live page before building the report.

**7 · Schema.** Flags per page: no JSON-LD type for the content (blog/case study), author not a Person,
team pages without Person/ProfilePage, visible FAQ without FAQPage, video without VideoObject, services
marked up as Product with self-given ratings, broken JSON. Site-wide: Organization fields and sameAs
consistency, rating values that differ between pages, llms.txt, AI bots in robots.txt.
Ready JSON-LD templates are in `references/schema_templates.json` and land on the last sheet.

**8 · Deliver.** Send the file (`SendUserFile`, display `attach`; otherwise give its full path). Then a
short summary in the person's language:
- what was audited (scope, pages, how many read by agents) and totals by priority;
- the 10–15 most damaging items with page paths (placeholders and editor notes left in, broken
  numbers, meaning-reversing typos, contradictions in company facts, wrong text copied from another page);
- the top schema gaps for AI search;
- what was NOT checked (images, visual layout, Rich Results Test validation) and that the "fix"
  column is a suggestion to confirm where it states a fact.
Never edit the site's texts unless asked.

## Lessons from the first run (mobidev.biz, 646 pages → 1 738 findings, 702 schema rows)
- Keep whitespace-only text nodes when extracting; dropping them created ~45 false "missing space" findings.
- Pages extracted but agents' quotes don't match → `unverified.json`, not the report.
- Template elements (badges, footers) repeat on hundreds of pages; collapse them to one row.
- Agents' "fix" sometimes guesses a fact (a year, a count) — say so.
