#!/usr/bin/env python3
"""Step 7. Structured-data (JSON-LD) audit for Google rich results and AI answer engines.

Usage: python3 -I schema_audit.py --site https://mobidev.biz --work WORK
Writes WORK/schema_pages.json  [[slug, priority, problem, fix, why], ...]
       WORK/schema_site.json   [[priority, where, problem, fix, why], ...]  (site-wide, data-driven)
       WORK/schema_inventory.json  {section: {type: page_count}}

Per page: unparseable JSON-LD; Product+AggregateRating used for a service (self-serving);
visible FAQ without FAQPage; duplicate FAQPage; embedded video without VideoObject;
blog without Article/BlogPosting or with a non-Person author; case study without Article;
testimonial on page without Review/Quotation; team page without Person/ProfilePage;
Service without provider; HowTo (no Google rich result since 2023).
Site-wide: Organization sameAs variants, missing Organization fields, rating values that differ
between pages, llms.txt presence/links/stale numbers, AI bots in robots.txt.
Section = first path segment; adjust SECTION names below for another site.
"""
import argparse, os, re, json, collections, subprocess

def nodes(raw):
    acc, err = [], 0
    def walk(o):
        if isinstance(o, dict):
            if '@type' in o: acc.append(o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    for b in re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', raw, re.S | re.I):
        try: walk(json.loads(b))
        except json.JSONDecodeError: err += 1
    return acc, err

T = lambda n: n['@type'] if isinstance(n['@type'], str) else '/'.join(n['@type'])
H, M, L = '1 Високий', '2 Середній', '3 Низький'
WHY = {
 'faq': 'Питання-відповідь — формат, який AI-пошук цитує найохочіше; без розмітки машина не відрізняє питання від відповіді',
 'blog': 'Автор, дата і тип контенту — головні сигнали E-E-A-T і свіжості, за якими AI-пошук обирає, кого цитувати',
 'case': 'Без типу контенту кейс для машини нічим не відрізняється від іншої сторінки; результати й галузь не видобуваються',
 'person': 'На ці сторінки посилаються автори; без Person вони не працюють як сутність-експерт для Google і LLM',
 'rating': 'Google не показує оцінки, які компанія ставить собі сама; різні цифри на різних сторінках підривають довіру до сутності',
}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--site', required=True); ap.add_argument('--work', required=True)
    a = ap.parse_args(); site = a.site.rstrip('/')
    rows, inv = [], collections.defaultdict(collections.Counter)
    sameas, ratings, org_fields, nologo = collections.Counter(), collections.defaultdict(list), collections.Counter(), []
    add = lambda *r: rows.append(list(r))
    for fn in sorted(os.listdir(f'{a.work}/html')):
        p = fn[:-5]; s = p.split('__')[0] if '__' in p else 'landing'
        raw = open(f'{a.work}/html/{fn}', encoding='utf-8', errors='ignore').read()
        ns, err = nodes(raw); types = [T(n) for n in ns]
        for t in set(types): inv[s][t] += 1
        faq_html = bool(re.search(r'class="[^"]*\bfaq', raw, re.I))
        video = bool(re.search(r'youtube\.com/embed|youtu\.be/|<video[\s>]|player\.vimeo', raw))
        if err: add(p, H, 'JSON-LD не парситься', 'Виправити синтаксис (кілька об’єктів — обгорнути в масив [...] або розбити на окремі <script>)', 'Невалідний блок повністю ігнорується')
        for n in ns:
            if T(n) == 'Organization' and str(n.get('@id', '')).endswith('#organization'):
                sameas[tuple(sorted(n.get('sameAs') or []))] += 1
                for k in ('logo', 'description', 'foundingDate', 'address', 'contactPoint', 'numberOfEmployees'): org_fields[(k, k in n)] += 1
                if 'logo' not in n: nologo.append(p)
            if T(n) == 'AggregateRating':
                ratings[f"{n.get('ratingValue')}/{n.get('reviewCount') or n.get('ratingCount')}"].append(p)
        if 'Product' in types and 'AggregateRating' in types and s not in ('product',):
            ar = next(n for n in ns if T(n) == 'AggregateRating')
            add(p, H, f"Послугу розмічено як Product з AggregateRating {ar.get('ratingValue')}/{ar.get('reviewCount') or ar.get('ratingCount')} без самих відгуків",
                'Product → Service (provider → #organization, serviceType, areaServed); рейтинг прибрати або дати одну цифру з Clutch', WHY['rating'])
        if faq_html and 'FAQPage' not in types: add(p, H if s in ('case-studies', 'services') else M, 'Видимий FAQ без FAQPage', 'Додати FAQPage з тими самими питаннями й відповідями', WHY['faq'])
        if types.count('FAQPage') > 1: add(p, M, 'Два FAQPage на сторінці', 'Залишити один', 'Помилка в Search Console')
        if video and 'VideoObject' not in types: add(p, M, 'Вбудоване відео без VideoObject', 'VideoObject: name, description, thumbnailUrl, uploadDate, embedUrl, duration, transcript', 'Відеоблоки Google, AI Overviews; транскрипт — текст для цитування')
        arts = [n for n in ns if T(n) in ('Article', 'BlogPosting', 'TechArticle', 'NewsArticle')]
        if s == 'blog':
            if not arts: add(p, H, 'Немає Article/BlogPosting — лише WebPage', 'BlogPosting: headline, image, datePublished, dateModified, author=Person(@id сторінки автора, jobTitle, sameAs LinkedIn), publisher=#organization', WHY['blog'])
            else:
                au = arts[0].get('author'); au = au[0] if isinstance(au, list) and au else au
                if not (isinstance(au, dict) and au.get('@type') == 'Person' and au.get('name')):
                    add(p, H, 'Article без author-Person', 'author → Person з name, url (/our-team/…), jobTitle, sameAs', WHY['blog'])
                elif not au.get('sameAs'): add(p, M, 'author без sameAs', 'Додати sameAs (LinkedIn)', 'Підтверджує реальну людину-експерта')
                if not arts[0].get('image'): add(p, L, 'Article без image', 'Додати image ≥1200px', 'Прев’ю в rich results і AI-відповідях')
        if s == 'case-studies':
            if not arts: add(p, H, 'Кейс розмічено лише як WebPage', 'Article (+additionalType CaseStudy): headline з результатом, дати, about → Service, mentions → клієнт (якщо публічний), keywords', WHY['case'])
            if re.search(r'testimonial', raw, re.I) and re.search(r'md-slider|single-testimonial', raw) and not ({'Review', 'Quotation'} & set(types)):
                add(p, M, 'Відгук/цитата без розмітки', 'Review (itemReviewed → #organization, author → Person з посадою) або Quotation', 'Розмічений відгук — одиниця довіри, яку легко процитувати')
        if s == 'our-team' and 'Person' not in types: add(p, H, 'Сторінка експерта без Person/ProfilePage', 'ProfilePage → Person (name, jobTitle, worksFor #organization, image, sameAs, knowsAbout)', WHY['person'])
        if any(T(n) == 'Service' and 'provider' not in n for n in ns): add(p, L, 'Service без provider', 'provider: {"@id": ".../#organization"}', 'Прив’язує послугу до компанії')
        if 'HowTo' in types: add(p, L, 'HowTo', 'Можна лишити, але rich result Google прибрав у 2023', 'Не шкодить, ефекту в Google немає')
    site_rows = []
    if len(sameas) > 1:
        top = sameas.most_common()
        site_rows.append([H, 'Organization.sameAs', f'{len(sameas)} різних списків sameAs; найчастіший ({top[0][1]} стор.): {", ".join(top[0][0]) or "порожній"}', 'Один повний список профілів у шаблоні на всіх сторінках', 'sameAs зв’язує сайт із профілями, які цитує AI (LinkedIn, Clutch, Reddit)'])
    total = sum(sameas.values())
    weak = [f'{k} ({org_fields[(k, True)]}/{total})' for k in ('description', 'foundingDate', 'address', 'contactPoint', 'numberOfEmployees') if org_fields[(k, True)] < total / 2]
    if weak: site_rows.append([H, 'Organization (#organization)', 'Поля є на меншості сторінок (є/всього): ' + ', '.join(weak), 'Винести повний вузол Organization у спільний шаблон, однаковий на всіх сторінках', 'З цього вузла моделі будують уявлення про компанію'])
    if nologo: site_rows.append([M, 'Organization.logo', f'Немає logo на {len(set(nologo))} стор.', 'Підтягнути logo в усі шаблони', 'Неповна сутність'])
    if len(ratings) > 1: site_rows.append([H, 'AggregateRating', 'Різні значення: ' + '; '.join(f'{k} ({len(v)} стор.)' for k, v in sorted(ratings.items(), key=lambda x: -len(x[1]))), 'Одна цифра з одного джерела (Clutch) або прибрати', WHY['rating']])
    cur = lambda u: subprocess.run(['curl', '-sSL', '-A', 'Mozilla/5.0', '-w', '\n%{http_code}', u], capture_output=True, text=True).stdout
    llms = cur(site + '/llms.txt'); body, code = llms.rsplit('\n', 1) if '\n' in llms else ('', llms)
    if code.strip() != '200': site_rows.append([M, 'llms.txt', 'Файлу немає', 'Створити за llmstxt.org: опис компанії + списки посилань на ключові сторінки', 'Карта сайту для AI-агентів'])
    else:
        n_links = len(re.findall(r'\]\(https?://', body))
        site_rows.append([M if n_links < 5 else L, 'llms.txt', f'Файл є, посилань на сторінки: {n_links}. Перевірити цифри вручну (роки, клієнти)', 'Додати секції з посиланнями: сервіси, кейси, гайди, експерти', 'Без посилань модель не знає, що читати далі'])
    robots = cur(site + '/robots.txt')
    bots = [b for b in ('GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'ClaudeBot', 'Google-Extended') if b not in robots]
    site_rows.append([M if bots else L, 'robots.txt', 'Не згадані: ' + ', '.join(bots) if bots else 'AI-боти дозволені', 'Перевірити також блокування на рівні CDN/WAF за логами', 'Інакше дозвіл у robots.txt нічого не дає'])
    json.dump(rows, open(f'{a.work}/schema_pages.json', 'w'), ensure_ascii=False, indent=0)
    json.dump(site_rows, open(f'{a.work}/schema_site.json', 'w'), ensure_ascii=False, indent=0)
    json.dump({k: dict(v) for k, v in inv.items()}, open(f'{a.work}/schema_inventory.json', 'w'), ensure_ascii=False, indent=0)
    print(len(rows), 'page rows,', len(site_rows), 'site rows')
    for (p, pr, prob, *_), n in collections.Counter((('', r[1], r[2][:55])) for r in rows).most_common(20): print(f'  {n:4d} {pr} {prob}')

if __name__ == '__main__':
    main()
