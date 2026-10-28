#!/usr/bin/env python3
"""Step 1. Find the pages to audit and download them into WORK/html/.

Usage:
  python3 -I crawl.py --url <link the user gave> --work WORK [--scope auto|site|section|page] [--workers 6]

Scope (auto = decided from the link):
  site    — link is the homepage            → every URL in the sitemap
  section — link ends with '/' or is a listing (e.g. /blog/) → sitemap URLs under that path
  page    — any other link                   → just that page
Sitemap discovery: robots.txt 'Sitemap:' lines, then /sitemap.xml, /sitemap_index.xml, /wp-sitemap.xml
(indexes followed). No sitemap → falls back to the page + same-site links found on it.
Writes WORK/site.json {site, scope, include}, WORK/urls.txt, WORK/html/<slug>.html, WORK/codes.txt.
slug = URL path with '/' → '__'; homepage = 'home'.
"""
import argparse, os, re, json, subprocess, concurrent.futures as cf
from urllib.parse import urlparse, urljoin

def get(u):
    r = subprocess.run(['curl', '-sSL', '--max-time', '60', '-A', 'Mozilla/5.0', '-w', '\n%{http_code}', u], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition('\n')
    return (body, code.strip()) if r.stdout else ('', '000')

def slug(u, site):
    return u[len(site):].split('#')[0].split('?')[0].strip('/').replace('/', '__') or 'home'

def sitemap_urls(site):
    robots, _ = get(site + '/robots.txt')
    todo = re.findall(r'(?im)^\s*sitemap:\s*(\S+)', robots) or [site + p for p in ('/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml')]
    seen, urls = set(), []
    while todo:
        sm = todo.pop(0)
        if sm in seen: continue
        seen.add(sm); body, code = get(sm)
        if code != '200': continue
        for loc in re.findall(r'<loc>\s*(?:<!\[CDATA\[)?\s*([^<\s\]]+)', body):
            (todo if re.search(r'\.xml(\.gz)?$', loc) else urls).append(loc)
        if urls and not todo: break
    return sorted(set(urls))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', required=True); ap.add_argument('--work', required=True)
    ap.add_argument('--scope', default='auto', choices=['auto', 'site', 'section', 'page'])
    ap.add_argument('--workers', type=int, default=6)
    a = ap.parse_args()
    link = a.url if '://' in a.url else 'https://' + a.url
    pu = urlparse(link); site = f'{pu.scheme}://{pu.netloc}'; path = pu.path or '/'
    scope = a.scope
    if scope == 'auto':
        scope = 'site' if path in ('', '/') else ('section' if path.endswith('/') or path.count('/') == 1 else 'page')
    os.makedirs(f'{a.work}/html', exist_ok=True)
    if scope == 'page':
        urls = [link.split('#')[0]]
    else:
        urls = sitemap_urls(site)
        if not urls:
            body, _ = get(link)
            urls = sorted({urljoin(link, h).split('#')[0] for h in re.findall(r'href="([^"]+)"', body)
                           if urljoin(link, h).startswith(site)} | {link})
            print('no sitemap found — using the page and its same-site links')
        if scope == 'section':
            pref = site + path.rstrip('/')
            sect = [u for u in urls if u.rstrip('/') == pref or u.startswith(pref + '/')]
            urls = sect or [link]
    urls = [u for u in urls if urlparse(u).netloc == pu.netloc]
    json.dump({'site': site, 'scope': scope, 'include': path}, open(f'{a.work}/site.json', 'w'))
    open(f'{a.work}/urls.txt', 'w').write('\n'.join(urls) + '\n')
    def one(u):
        f = f'{a.work}/html/{slug(u, site)}.html'
        if os.path.exists(f) and os.path.getsize(f) > 0: return f'cached {u}'
        r = subprocess.run(['curl', '-sSL', '--max-time', '60', '-A', 'Mozilla/5.0', '-o', f, '-w', '%{http_code}', u], capture_output=True, text=True)
        return f'{r.stdout or "000"} {u}'
    with cf.ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(one, urls))
    open(f'{a.work}/codes.txt', 'w').write('\n'.join(res) + '\n')
    bad = [r for r in res if not r.startswith(('200', 'cached'))]
    for r in bad:
        f = f"{a.work}/html/{slug(r.split(' ', 1)[1], site)}.html"
        if os.path.exists(f): os.remove(f)
    print(f'site={site} scope={scope} urls={len(urls)} failed={len(bad)}'); [print(' ', b) for b in bad[:20]]

if __name__ == '__main__':
    main()
