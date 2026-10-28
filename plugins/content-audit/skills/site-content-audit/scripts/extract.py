#!/usr/bin/env python3
"""Step 2. Turn WORK/html/*.html into readable main-content text + page metadata.

Usage: python3 -I extract.py --work WORK [--stop-regex 'text that starts the site footer']
Writes WORK/txt/<slug>.txt and WORK/txt/_meta.json.

Main content = everything except <nav>, <footer>, <aside>, and the site-wide <header>
(role=banner, or id/class containing 'header'/'masthead'/'site-header' when it sits outside <main>/<article>),
starting at the first <h1> when there is one. --stop-regex cuts at a footer-like block that is not
inside a <footer> tag (on mobidev.biz: 'Get Fresh').
Text format: '<H1> …' headings, '• ' list items, "[IMG alt='…']" alts, ⟦href⟧ link markers.

Lesson learned: whitespace-only text nodes are KEPT. Dropping them glues words from adjacent inline
tags ('captivating</span> <span>and' → 'captivatingand') and creates false 'missing space' findings.
"""
import argparse, os, re, json, html as H
from html.parser import HTMLParser

DROP = ('script', 'style', 'noscript', 'svg', 'template')
CHROME = ('nav', 'footer', 'aside')
BLOCK = ('p', 'li', 'div', 'section', 'br', 'tr', 'blockquote', 'button', 'td', 'th', 'dd', 'dt', 'figcaption')
VOID = ('br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'col', 'embed', 'track')

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.out = []; s.skip = []; s.content_depth = 0
    def _skipping(s): return bool(s.skip)
    def handle_starttag(s, t, a):
        a = dict(a); attrs = ' '.join(str(v) for v in a.values() if v).lower()
        if t in VOID:
            if not s.skip:
                if t == 'img': s.out.append(f"\n[IMG alt='{a.get('alt', '')}']\n")
                elif t == 'br': s.out.append('\n')
            return
        if s.skip:
            if t == s.skip[-1][0]: s.skip[-1][1] += 1
            return
        if t in ('main', 'article'): s.content_depth += 1
        site_header = t == 'header' and (a.get('role') == 'banner' or (s.content_depth == 0 and re.search(r'header|masthead|banner', attrs)))
        if t in DROP or t in CHROME or site_header or a.get('role') in ('navigation', 'contentinfo'):
            s.skip.append([t, 1]); return
        if t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'): s.out.append(f'\n<{t.upper()}> ')
        elif t == 'a' and a.get('href'): s.out.append(f"⟦{a['href']}⟧")
        elif t in BLOCK: s.out.append('\n')
        if t == 'li': s.out.append('• ')
    def handle_endtag(s, t):
        if s.skip:
            if t == s.skip[-1][0]:
                s.skip[-1][1] -= 1
                if s.skip[-1][1] == 0: s.skip.pop()
            return
        if t in ('main', 'article'): s.content_depth = max(0, s.content_depth - 1)
        if t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') or t in BLOCK: s.out.append('\n')
    def handle_data(s, d):
        if not s.skip: s.out.append(re.sub(r'\s+', ' ', d))   # keep whitespace-only nodes

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--work', required=True); ap.add_argument('--stop-regex', default='')
    a = ap.parse_args()
    src, dst = f'{a.work}/html', f'{a.work}/txt'; os.makedirs(dst, exist_ok=True); meta = {}
    for fn in sorted(os.listdir(src)):
        if not fn.endswith('.html'): continue
        raw = open(os.path.join(src, fn), encoding='utf-8', errors='ignore').read()
        p = P(); p.feed(raw)
        lines = [l for l in re.sub(r'[ \t]*\n\s*', '\n', ''.join(p.out)).split('\n')]
        i = next((k for k, l in enumerate(lines) if l.startswith('<H1>')), 0)
        j = next((k for k, l in enumerate(lines) if a.stop_regex and k > i and re.search(a.stop_regex, l)), len(lines))
        body = '\n'.join(l.strip() for l in lines[i:j] if l.strip())
        open(os.path.join(dst, fn[:-5] + '.txt'), 'w').write(body)
        g = lambda r: (H.unescape(m.group(1).strip()) if (m := re.search(r, raw, re.S | re.I)) else None)
        meta[fn[:-5]] = dict(
            title=g(r'<title[^>]*>(.*?)</title>'),
            desc=g(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)') or g(r'<meta\s+content=["\']([^"\']*)["\']\s+name=["\']description'),
            h1=len(re.findall(r'<h1[\s>]', raw, re.I)), canon=g(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)'),
            robots=g(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']+)'),
            pub=g(r'"datePublished"\s*:\s*"([^"T]+)'), mod=g(r'"dateModified"\s*:\s*"([^"T]+)'),
            words=len(re.sub(r'⟦[^⟧]*⟧', '', body).split()))
    json.dump(meta, open(f'{dst}/_meta.json', 'w'), ensure_ascii=False, indent=0)
    empty = [k for k, v in meta.items() if v['words'] < 30]
    print(len(meta), 'pages extracted;', len(empty), 'with <30 words of main text (check extraction or real thin pages):', empty[:10])

if __name__ == '__main__':
    main()
