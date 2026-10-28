# content-audit (plugin)

Надішліть Claude посилання і напишіть «зроби аудит контенту». Отримаєте Excel-звіт:
описки, граматика, плейсхолдери, зламаний текст, нестиковки, застарілі твердження,
суперечливі факти про компанію, title/meta, і аудит schema (JSON-LD) для Google та AI-пошуку,
з точними цитатами, порадою «як виправити» і колонкою статусу.

- Посилання на головну → увесь сайт (за sitemap.xml)
- Посилання на розділ (`/blog`, `/case-studies/`) → лише цей розділ
- Посилання на конкретну сторінку → лише вона

Встановлення (Claude Code):
```
/plugin install content-audit --marketplace mobidev-mrkt/landing#skills
```
або `/plugin marketplace add mobidev-mrkt/landing#skills`, потім `/plugin install content-audit@mobidev-skills`.
Детально: README.md і METHODOLOGY.md у корені гілки `skills`.

Працює в Claude Code (desktop, CLI або claude.ai/code). Потрібен доступ до сайту з сесії; у хмарній
сесії домен сайту має бути дозволений у мережевих налаштуваннях середовища.
Великі сайти вичитуються паралельними агентами і займають від 15 хв до години.
