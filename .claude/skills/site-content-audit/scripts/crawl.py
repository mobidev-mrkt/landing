#!/usr/bin/env python3
"""Step 1. Download every URL from the site's sitemap into WORK/html/.

Usage: python3 -I crawl.py --site https://mobidev.biz --work WORK [--workers 6]
Writes WORK/urls.txt, WORK/html/<slug>.html (slug = path with '/' -> '__', home = 'home'),
WORK/codes.txt (HTTP status per URL). Follows sitemap indexes. Uses curl (respects the proxy).
"""
import argparse, os, re, subprocess, concurrent.futures as cf

def slug(url, site):
    p = url[len(site):].strip('/')
    return p.replace('/', '__') or 'home'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--site', required=True); ap.add_argument('--work', required=True)
    ap.add_argument('--workers', type=int, default=6)
    a = ap.parse_args(); site = a.site.rstrip('/')
    os.makedirs(f'{a.work}/html', exist_ok=True)
    todo, urls = [site + '/sitemap.xml'], []
    while todo:
        sm = subprocess.run(['curl', '-sSL', '-A', 'Mozilla/5.0', todo.pop()], capture_output=True, text=True).stdout
        for loc in re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', sm):
            (todo if loc.endswith('.xml') else urls).append(loc)
    urls = sorted(set(u for u in urls if u.startswith(site)))
    open(f'{a.work}/urls.txt', 'w').write('\n'.join(urls) + '\n')
    def one(u):
        f = f'{a.work}/html/{slug(u, site)}.html'
        if os.path.exists(f) and os.path.getsize(f) > 0: return f'cached {u}'
        code = subprocess.run(['curl', '-sSL', '-A', 'Mozilla/5.0', '-o', f, '-w', '%{http_code}', u],
                              capture_output=True, text=True).stdout
        return f'{code} {u}'
    with cf.ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(one, urls))
    open(f'{a.work}/codes.txt', 'w').write('\n'.join(res) + '\n')
    bad = [r for r in res if not r.startswith(('200', 'cached'))]
    print(f'{len(urls)} urls, {len(bad)} non-200'); [print(' ', b) for b in bad[:20]]

if __name__ == '__main__':
    main()
