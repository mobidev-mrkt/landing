#!/usr/bin/env python3
"""Step 6. Merge agent findings, verify every quote against the page text, collapse template repeats.

Usage: python3 -I verify_merge.py --site https://mobidev.biz --work WORK
Reads  WORK/out/*.jsonl (agent output), WORK/txt/*.txt
Writes WORK/findings.json (verified, deduplicated) and WORK/cross_facts.json (company claims).

A finding is kept only if its quote (whitespace/quote-normalised) is found in that page's
title, meta description or body. Rows whose quote cannot be found are written to
WORK/unverified.json for a human look — they are NOT shipped. Identical findings on >=4 pages
become one 'template' row (fix once in the theme).
"""
import argparse, os, re, json, glob, collections

def nz(x):
    x = re.sub(r'⟦[^⟧]*⟧', '', x or '')
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), (' ', ' ')): x = x.replace(a, b)
    return re.sub(r'\s+', ' ', x).strip().lower()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--site', required=True); ap.add_argument('--work', required=True)
    a = ap.parse_args(); site = a.site.rstrip('/') + '/'
    meta = json.load(open(f'{a.work}/txt/_meta.json')); cache = {}
    def page_text(url):
        k = url.replace(site, '').strip('/').replace('/', '__') or 'home'
        if k not in cache:
            f = f'{a.work}/txt/{k}.txt'; m = meta.get(k)
            body = open(f).read() if os.path.exists(f) else ''
            cache[k] = nz(body + ' ' + str(m.get('title')) + ' ' + str(m.get('desc'))) if m else None
        return cache[k]
    rows, facts, bad = [], [], []
    for f in sorted(glob.glob(f'{a.work}/out/*.jsonl')):
        for l in open(f):
            l = l.strip()
            if not l: continue
            try: r = json.loads(l)
            except json.JSONDecodeError: continue
            if r.get('category') == 'cross_fact': facts.append(r); continue
            t, q = page_text(r.get('url', '')), nz(re.sub(r'^(TITLE|META DESCRIPTION):\s*', '', r.get('quote', '')))
            (rows if t and q and q in t else bad).append(r)
    grp = collections.defaultdict(list)
    for r in rows: grp[(nz(r['quote'])[:80], r['category'])].append(r)
    out = []
    for g in grp.values():
        urls = sorted(set(x['url'] for x in g))
        if len(urls) >= 4:
            r = dict(g[0]); r['template_pages'] = urls; out.append(r)
        else:
            seen = set()
            for x in g:
                if x['url'] not in seen: seen.add(x['url']); out.append(x)
    json.dump(out, open(f'{a.work}/findings.json', 'w'), ensure_ascii=False, indent=0)
    json.dump(facts, open(f'{a.work}/cross_facts.json', 'w'), ensure_ascii=False, indent=0)
    json.dump(bad, open(f'{a.work}/unverified.json', 'w'), ensure_ascii=False, indent=0)
    print(f'{len(out)} findings kept, {len(bad)} unverified (see unverified.json), {len(facts)} company claims')
    print(collections.Counter((r['category'], r['severity']) for r in out).most_common())

if __name__ == '__main__':
    main()
