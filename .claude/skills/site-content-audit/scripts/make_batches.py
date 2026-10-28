#!/usr/bin/env python3
"""Step 4. Pack page texts into proofreading batches for parallel agents.

Usage: python3 -I make_batches.py --site https://mobidev.biz --work WORK [--words 24000]
Writes WORK/batches/<group>NN.txt  (group 'p' = non-blog pages, 'k' = blog posts).
Each page block: '========== PAGE: <url>' + TITLE + META DESCRIPTION + text without link markers.
~24-30k words per batch keeps one agent's context comfortable and lets it read everything.
"""
import argparse, os, re, json

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--site', required=True); ap.add_argument('--work', required=True)
    ap.add_argument('--words', type=int, default=24000); ap.add_argument('--blog-prefix', default='blog__')
    a = ap.parse_args(); site = a.site.rstrip('/') + '/'
    meta = json.load(open(f'{a.work}/txt/_meta.json')); os.makedirs(f'{a.work}/batches', exist_ok=True)
    groups = {'p': [k for k in sorted(meta) if not k.startswith(a.blog_prefix)],
              'k': [k for k in sorted(meta) if k.startswith(a.blog_prefix)]}
    for g, pages in groups.items():
        batches, cur, w = [], [], 0
        for k in pages:
            t = re.sub(r'⟦[^⟧]*⟧', '', open(f'{a.work}/txt/{k}.txt').read())
            t = re.sub(r"\n\[IMG alt=''\]", '', t)
            url = site + ('' if k == 'home' else k.replace('__', '/'))
            block = f"\n\n========== PAGE: {url}\nTITLE: {meta[k]['title']}\nMETA DESCRIPTION: {meta[k]['desc']}\n----------\n{t}"
            n = len(block.split())
            if cur and w + n > a.words: batches.append(cur); cur, w = [], 0
            cur.append(block); w += n
        if cur: batches.append(cur)
        for i, c in enumerate(batches): open(f'{a.work}/batches/{g}{i:02d}.txt', 'w').write(''.join(c))
        print(g, len(pages), 'pages ->', len(batches), 'batches')

if __name__ == '__main__':
    main()
