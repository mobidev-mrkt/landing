#!/usr/bin/env python3
"""Step 3. Deterministic checks over every page (cheap, catches what readers miss).

Usage: python3 -I auto_checks.py --work WORK
Writes WORK/auto.json  {check_name: [[slug, text], ...]}
       WORK/spell_candidates.json  [[word, likely_fix, slug, context], ...]  (needs pyspellchecker)

Checks: leftover [brackets]/TODO/TBA/lorem, mojibake, Cyrillic letters inside Latin words
(SEO-invisible), repeated words, space before punctuation, missing space after a period,
'%' with the number missing (alt bug), brand casing, dangling 'list intro:' lines,
missing/long/duplicate title & description, H1 count != 1.
Spell candidates: rare words (<=2 uses site-wide) not in the dictionary whose 1-edit
neighbour is common on the same site (>=15 uses). Curate by hand into spell_confirmed.json.
"""
import argparse, os, re, json, collections

CYR = r'[А-Яа-яЁёІіЇїЄєҐґ]'
MIXED = rf'\b\w*(?:[A-Za-z]{CYR}|{CYR}[A-Za-z])\w*\b'

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--work', required=True)
    ap.add_argument('--brand', default='', help='exact brand spelling, e.g. MobiDev (optional)'); a = ap.parse_args()
    D = f'{a.work}/txt'; meta = json.load(open(f'{D}/_meta.json'))
    F = collections.defaultdict(list)
    add = lambda c, p, t: F[c].append([p, t.strip()[:240]])
    freq, occ = collections.Counter(), {}
    for fn in sorted(os.listdir(D)):
        if not fn.endswith('.txt'): continue
        p = fn[:-4]; vis = re.sub(r'⟦[^⟧]*⟧', '', open(f'{D}/{fn}').read())
        for m in re.finditer(MIXED, vis):
            add('cyrillic_in_latin', p, f"{m.group(0)} :: {vis[max(0, m.start()-40):m.end()+30]}".replace('\n', ' '))
        lines = [l.strip() for l in vis.split('\n') if l.strip()]
        for L, nxt in zip(lines, lines[1:] + ['<END>']):
            for mm in re.finditer(r'\[(?!IMG)[^\]\n]{2,90}\]', L):
                if not re.fullmatch(r'\[\d{1,2}(:\d\d){1,2}\]|\[\d+\]', mm.group(0)): add('brackets', p, L)
            if re.search(r'\b(TODO|TBD|TBA|lorem|ipsum|XXX+|PLACEHOLDER)\b|\{\{|\}\}|\?\?\?|re-verify|to confirm', L, re.I): add('placeholder_words', p, L)
            if re.search(r'â€|Ã.|�', L): add('mojibake', p, L)
            for mm in re.finditer(r'\b([A-Za-z]{2,})\s+\1\b', L, re.I):
                if mm.group(1).lower() not in ('that', 'had', 'is', 'very', 'no', 'so', 'ha', 'bye'): add('repeated_word', p, f'{mm.group(0)} :: {L}')
            if re.search(r'\w\s[,.;:!?](\s|$)', L): add('space_before_punct', p, L)
            for mm in re.finditer(r'\b[a-z]{3,}[.,][A-Z][a-z]{2,}\b', L):
                if not re.search(r'\.(js|io|ai|NET|com|net|org|biz)', mm.group(0)): add('missing_space_after_punct', p, f'{mm.group(0)} :: {L}')
            if re.search(r"(by|to|of|up to|increased|decreased|reduced|grew)\s+%", L, re.I) and 'IMG' in L: add('alt_number_missing', p, L)
            if a.brand and not L.startswith('[IMG') and any(m.group(0) != a.brand for m in re.finditer(rf'\b{a.brand}\b', L, re.I)): add('brand_casing', p, L)
            if L.endswith(':') and len(L) > 25 and (nxt.startswith('<H') or nxt == '<END>'): add('dangling_colon', p, f'{L}  →  {nxt[:60]}')
            if not (re.search(r'[{};=<>]|\(\)|//', L) and not L.startswith('<H')):
                for w in re.findall(r"(?<![\w@./'’-])([a-z]{4,})(?![\w@/'’-])", L):
                    freq[w] += 1; occ.setdefault(w, (p, L[:170]))
    titles, descs = collections.defaultdict(list), collections.defaultdict(list)
    for p, v in meta.items():
        if not v['title']: add('meta_missing_title', p, '')
        else:
            titles[v['title']].append(p)
            if len(v['title']) > 70: add('meta_title_long', p, f"{len(v['title'])}: {v['title']}")
        if not v['desc'] or v['desc'] == 'None': add('meta_missing_desc', p, v['desc'] or '')
        else:
            descs[v['desc']].append(p)
            if len(v['desc']) > 170: add('meta_desc_long', p, f"{len(v['desc'])}: {v['desc'][:120]}")
        if v['h1'] != 1: add('h1_count', p, f"h1={v['h1']}")
    for t, ps in titles.items():
        if len(ps) > 1: [add('meta_dup_title', x, t) for x in ps]
    for t, ps in descs.items():
        if len(ps) > 1: [add('meta_dup_desc', x, t[:140]) for x in ps]
    json.dump(F, open(f'{a.work}/auto.json', 'w'), ensure_ascii=False, indent=0)
    for k, v in sorted(F.items(), key=lambda x: -len(x[1])): print(f'{k:28s} {len(v):5d}')
    try:
        from spellchecker import SpellChecker
    except ImportError:
        print('pyspellchecker not installed: pip install pyspellchecker  (spell candidates skipped)'); return
    sp = SpellChecker(distance=1); L26 = 'abcdefghijklmnopqrstuvwxyz'
    def e1(w):
        s = [(w[:i], w[i:]) for i in range(len(w) + 1)]
        return set([x + y[1:] for x, y in s if y] + [x + y[1] + y[0] + y[2:] for x, y in s if len(y) > 1]
                   + [x + c + y[1:] for x, y in s if y for c in L26] + [x + c + y for x, y in s for c in L26])
    out = []
    for w in sp.unknown([w for w in freq if freq[w] <= 2]):
        c = [(freq[x], x) for x in e1(w) if freq[x] >= 15 and x != w]
        if c: out.append([w, max(c)[1], *occ[w]])
    json.dump(sorted(out, key=lambda r: r[2]), open(f'{a.work}/spell_candidates.json', 'w'), ensure_ascii=False, indent=0)
    print(len(out), 'spell candidates -> curate into spell_confirmed.json {"wrong":"right"}')

if __name__ == '__main__':
    main()
