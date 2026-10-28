#!/usr/bin/env python3
"""Step 2. Turn WORK/html/*.html into readable main-content text + page metadata.

Usage: python3 -I extract.py --work WORK
Writes WORK/txt/<slug>.txt and WORK/txt/_meta.json.

Text format: '<H1> ...' heading lines, '• ' list items, "[IMG alt='...']" image alts,
links as ⟦href⟧ markers (strip them before quoting). Main content = from the first <H1>
to the footer marker (FOOTER_RE) — tune it for another site.

IMPORTANT (lesson learned): keep whitespace-only text nodes. Dropping them glues words
that sit in adjacent inline tags ("captivating</span> <span>and" -> "captivatingand")
and produces dozens of false "missing space" findings.
"""
import argparse, os, re, json, html as H
from html.parser import HTMLParser

FOOTER_RE = r'Get Fresh|GET FRESH INSIGHTS'
SKIP = ('script', 'style', 'noscript', 'svg', 'template')
BLOCK = ('p', 'li', 'div', 'section', 'br', 'tr', 'blockquote', 'button', 'td', 'th')

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.out = []; s.skip = 0
    def handle_starttag(s, t, a):
        a = dict(a)
        if t in SKIP: s.skip += 1
        if s.skip: return
        if t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'): s.out.append(f'\n<{t.upper()}> ')
        elif t == 'img': s.out.append(f"\n[IMG alt='{a.get('alt', '')}']\n")
        elif t == 'a' and a.get('href'): s.out.append(f"⟦{a['href']}⟧")
        elif t in BLOCK: s.out.append('\n')
        if t == 'li': s.out.append('• ')
    def handle_endtag(s, t):
        if t in SKIP: s.skip = max(0, s.skip - 1)
    def handle_data(s, d):
        if not s.skip: s.out.append(re.sub(r'\s+', ' ', d))   # keep whitespace-only nodes!

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--work', required=True); a = ap.parse_args()
    src, dst = f'{a.work}/html', f'{a.work}/txt'; os.makedirs(dst, exist_ok=True); meta = {}
    for fn in sorted(os.listdir(src)):
        raw = open(os.path.join(src, fn), encoding='utf-8', errors='ignore').read()
        p = P(); p.feed(raw)
        t = re.sub(r'[ \t]*\n\s*', '\n', ''.join(p.out))
        lines = t.split('\n')
        i = next((k for k, l in enumerate(lines) if l.startswith('<H1>')), 0)
        j = next((k for k, l in enumerate(lines) if k > i and re.search(FOOTER_RE, l)), len(lines))
        body = '\n'.join(lines[i:j]).strip()
        open(os.path.join(dst, fn[:-5] + '.txt'), 'w').write(body)
        g = lambda r: (H.unescape(m.group(1).strip()) if (m := re.search(r, raw, re.S | re.I)) else None)
        meta[fn[:-5]] = dict(
            title=g(r'<title>(.*?)</title>'), desc=g(r'<meta name="description" content="([^"]*)"'),
            h1=len(re.findall(r'<h1[\s>]', raw, re.I)), canon=g(r'<link rel="canonical" href="([^"]+)"'),
            robots=g(r'<meta name="robots" content="([^"]+)"'),
            pub=g(r'"datePublished":"([^"T]+)'), mod=g(r'"dateModified":"([^"T]+)'),
            words=len(re.sub(r'⟦[^⟧]*⟧', '', body).split()))
    json.dump(meta, open(f'{dst}/_meta.json', 'w'), ensure_ascii=False, indent=0)
    print(len(meta), 'pages extracted')

if __name__ == '__main__':
    main()
