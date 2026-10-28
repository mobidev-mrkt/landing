#!/usr/bin/env python3
"""Step 4. Pack page texts into proofreading batches for parallel agents.

Usage: python3 -I make_batches.py --work WORK [--words 24000]
Writes WORK/batches/<group>NN.txt  (group 'p' = non-blog pages, 'k' = blog posts).
Each page block: '========== PAGE: <url>' + TITLE + META DESCRIPTION + text without link markers.
~24-30k words per batch keeps one agent's context comfortable and lets it read everything.
"""
import argparse, os, re, json

BLOG_SEGMENTS = ('blog', 'articles', 'insights', 'news', 'posts', 'resources', 'journal', 'stories', 'trends-and-insights')
def seg(slug): return slug.split('__')[0] if '__' in slug else ('' if slug == 'home' else 'landing')
def is_blog(slug): return '__' in slug and seg(slug) in BLOG_SEGMENTS

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--work', required=True); ap.add_argument('--words', type=int, default=24000)
    a = ap.parse_args(); site = json.load(open(f'{a.work}/site.json'))['site'] + '/'
    meta = json.load(open(f'{a.work}/txt/_meta.json')); os.makedirs(f'{a.work}/batches', exist_ok=True)
    groups = {'p': [k for k in sorted(meta) if not is_blog(k) and meta[k]['words'] > 0],
              'k': [k for k in sorted(meta) if is_blog(k) and meta[k]['words'] > 0]}
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
