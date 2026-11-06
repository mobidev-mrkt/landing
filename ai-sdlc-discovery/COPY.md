# Free AI SDLC Readiness Review: копі сторінки

Сторінка: `mobidev.biz/?post_type=flexible&p=59932`
Трафік: YouTube Shorts з архітекторами MobiDev. Холодний, з мобільного, бачив конкретну людину.
Тип сторінки: campaign landing (Service Page Kit без навігації, одна дія).
Одна дія: **Book my free review** (форма). М'яка альтернатива: чекліст, у кінці сторінки.

Позначки в тексті:
- `[CONFIRM: …]` означає факт, який треба підтвердити з delivery або архітекторами. Я нічого не вигадував, тому ці місця лишаються видимими.
- `[VISUAL: …]` означає, що тут потрібна картинка чи компонент.

Перед публікацією в тексті не має лишитися жодної квадратної дужки.

---

## 0. Блокери (без цього сторінку не запускати)

1. **Тривалість дзвінка.** Скрізь у тексті стоїть `[CONFIRM: 30]` хвилин.
2. **Що людина отримує письмово** після дзвінка і в які строки (`[CONFIRM: written summary within 2 business days]`).
3. **З чого складається readiness score**: які 4–5 вимірів і яка шкала.
4. **«9.1 NPS».** Це або «9.1/10 client satisfaction», або реальний NPS (тоді число зовсім інше). Як є зараз, публікувати не можна.
5. **Кому підходить**: мінімальний розмір команди (`[CONFIRM: 10+ engineers]`).
6. **Одна історія з цифрою** (case card) і **одна цитата клієнта** (Clutch). Якщо їх немає, блок 6 скорочується до цифр і логотипів.
7. **Скільки слотів на тиждень** (для рядка про обмеження). Якщо обмеження немає, рядок видаляємо. Вигадана дефіцитність гірша, ніж її відсутність.
8. **Форма.** Залишаємо 3 поля + 1 необов'язкове (див. блок 1). Решту питань переносимо на thank-you сторінку.

---

## 1. Hero

`[VISUAL: hero. Ліворуч текст, праворуч форма. На мобільному порядок такий: eyebrow → H1 → картка спікера → форма → підзаголовок.]`

**Eyebrow** (змінюється за `utm_content` з кожного Short):

| utm_content | Текст |
|---|---|
| `yevhen` | Saw Yevhen on Shorts? He runs these reviews. |
| `iurii` | Saw Iurii on Shorts? He runs these reviews. |
| `rustam` | Saw Rustam on Shorts? He runs these reviews. |
| (без мітки) | Run by MobiDev solutions architects |

**H1**
> Free AI SDLC readiness review: find out where AI slows your delivery

**Підзаголовок**
> Your team has AI coding tools. Releases still ship at the same pace. A Claude Certified Architect reads your answers before the call, then spends [CONFIRM: 30] minutes with you on the few things holding your releases back. You leave with a readiness score and a list of what to fix first.

**Картка спікера** (під H1, фото та ім'я змінюються за тією самою `utm_content`)
`[VISUAL: кругле фото 56px, зелена обводка, як у блоці експертів]`
> **Yevhen Kuzminov**
> Solutions Architect · Claude Certified Architect

**Рядок ціни** (під карткою, дрібним текстом)
> Free. The call is with an architect, and you keep the score whatever you decide next.

### Форма

| Поле | Тип | Обов'язкове |
|---|---|---|
| Work email | email | так |
| First name | text | так |
| Which AI coding tools does your team use? | select: Copilot · Cursor · Claude Code · Several of these · Other · None yet | так |
| Where does AI break down for you? | textarea, 2 рядки | **ні**, плейсхолдер: *e.g. "PRs got bigger, reviews got slower"* |

Питання «How old is your core codebase?» переїжджає на thank-you сторінку разом з іншими кваліфікаційними питаннями.

**Кнопка:** `Book my free review`

**Під кнопкою:**
> 20 seconds now. On the next screen you pick a time and answer four short questions about how you ship.

**Згода (без змін):**
> ☐ I agree to receive other communications from MobiDev.
> By submitting this form, you agree with our Privacy Policy and Cookie policy.

---

## 1a. Trust strip (одразу під hero, на світлому фоні)

> **120+** legacy projects modernized · **65+** AI & ML products delivered · **[CONFIRM: 9.1/10]** client satisfaction, 2025 survey

`[VISUAL: рядок логотипів клієнтів MobiDev (Verizon Media, SMS group, discover.swiss, Camino, LMN та ін., файли є в репозиторії), сірі, у marquee]`

Підпис під логотипами, дрібно:
> Some of the companies MobiDev has built and modernized software for.

(Цей підпис потрібен, бо ці клієнти не проходили саме цей review. Без підпису виглядатиме, ніби проходили.)

---

## 2. Sounds familiar?

**H2:** Sounds familiar?

**Лід:**
> If two or more of these describe your team, the review is worth your time. [CONFIRM: звірити формулювання з реальними дзвінками; лапки ставити лише над дослівними фразами клієнтів]

- You rolled out Copilot to everyone, and six months later release frequency hasn't moved.
- PRs got bigger, and review became the bottleneck.
- AI works well on new modules and struggles with your ten-year-old core.
- Leadership asks whether the AI spend pays off, and you can't show them a number.
- Security wants to know what code goes to the model, and nobody owns that answer.

**Межа (одразу під списком, звичайним текстом):**
> This review is for teams with a production codebase and [CONFIRM: 10+] engineers. If you're still picking your first AI tool or haven't shipped a product yet, the checklist at the bottom of this page will serve you better than a call.

---

## 3. What you leave with

**H2:** What you leave with

`[VISUAL: зразок звіту, розмитий, як «документ» у правій колонці. Підпис "Sample, client details removed". Якщо реального зразка немає, не малювати фейковий, а прибрати візуал і залишити тільки список.]`

1. **An AI readiness score** across [CONFIRM: codebase, tooling, code review and testing, delivery process, governance]. You see where you stand on each, on one page.
2. **Your two or three real bottlenecks**, each with where it shows up in your pipeline and why it holds releases back.
3. **A fix-first list** for the next 30 days, ordered by impact, written so your team can act on it without us.
4. **[CONFIRM: a written summary in your inbox within 2 business days]**

**What this review doesn't include:**
> We don't need access to your repository, and we don't audit your code line by line. We also won't sell you a tool. If you want help with what we find, that's a separate conversation with a separate quote. Plenty of teams take the list and fix it themselves.

**Наша позиція** (виділений рядок або pull quote від архітектора):
> "In most reviews the coding tool turns out to be the smallest part of the problem. Code review, test coverage and an old core decide whether AI speeds a team up." [CONFIRM: погодити з Євгеном як його цитату]

---

## 4. How it works

**H2:** How it works

**01 · About two minutes from you**
> Leave your email (20 seconds) and pick a time. Then answer four short questions about how your team ships today: codebase age, tools, review process, release cadence.

**02 · The architect does the homework**
> Before you meet, the architect goes through your answers and prepares questions, so the whole call is spent on your bottlenecks.

**03 · [CONFIRM: 30] minutes on the call**
> You get your score, the bottlenecks behind it and the fix-first list. [CONFIRM: The written summary follows within 2 business days.]

Inline-кнопка під кроками (текстове посилання, той самий якір, що й форма):
> Book my free review ↑

---

## 5. Who you'll talk to

**H2:** Who you'll talk to

**Лід:**
> Your call is with one of these three architects. If you came from one of their Shorts, we book you with that person by default.

| Фото | Ім'я | Роль | Рядок про досвід |
|---|---|---|---|
| ✓ | Yevhen Kuzminov | Solutions Architect · Claude Certified Architect | [CONFIRM: N years, на чому спеціалізується, напр. "legacy .NET and Java modernization"] |
| ✓ | Iurii Luchaninov | Solutions Architect | [CONFIRM: N years, спеціалізація] |
| ✓ | Rustam Irzaev | Solutions Architect · Claude Certified Architect | [CONFIRM: N years, спеціалізація] |

Під кожною карткою можна додати посилання на LinkedIn [CONFIRM, чи погоджуються].

Якщо в Iurii немає сертифікації, це нормально. Не дописувати її.

---

## 6. Proof

**H2:** What this looks like in practice

`[VISUAL: case card]`
> **[CONFIRM: назва клієнта або "A US logistics platform"]**
> [CONFIRM: що було → що змінили → цифра. Напр. "Cycle time dropped from X to Y days after we …"]
> Read the case →

`[VISUAL: quote card з Clutch]`
> "[CONFIRM: дослівна цитата з Clutch-відгуку про AI або модернізацію]"
> — [CONFIRM: ім'я, посада, компанія]

Якщо кейсу і цитати поки немає, видаліть блок 6 цілком. Trust strip з цифрами вже стоїть угорі, і порожній блок proof гірший, ніж його відсутність.

---

## 7. FAQ

**H2:** Questions people ask before booking

**Is it actually free? What's the catch?**
> It's free. Some teams ask us to help with what the review turns up, and that's the business reason we run these. If you don't, you still keep the score and the list.

**Will the call turn into a sales pitch?**
> The call is run by an architect, and it's about your delivery. If you want to know how we could help, ask at the end. [CONFIRM: що реально відбувається після дзвінка, follow-up від sales чи ні]

**How much time does it take?**
> 20 seconds for the form, about two minutes for the four questions after it, [CONFIRM: 30] minutes on the call.

**Do you need access to our code?**
> No. We work from your answers and the conversation. If you'd like an NDA before the call, ask for one in the form. [CONFIRM: що NDA підписується за запитом]

**We haven't adopted AI tools yet. Is this still useful?**
> If you have a production codebase, yes: the score shows where AI would help first and what to fix before you roll it out. If you don't have one yet, start with the checklist below.

**Which tools do you cover?**
> Copilot, Cursor, Claude Code and the rest. The tool is one line of the score. Most of the review is about how code moves from a branch to production.

**What happens after the call?**
> [CONFIRM: You get the written summary within 2 business days.] If you want help fixing what we found, we'll scope it separately. If not, that's the end of it.

`[TECH: FAQPage schema на цей блок]`

---

## 8. Not ready for a call? (м'яка альтернатива, переїхала в кінець)

`[VISUAL: банер, фон з попередньої відповіді: linear-gradient(90deg, #0a1f1a 0%, #0d4f48 50%, #12B292 100%), праворуч обкладинка чекліста]`

**Заголовок:** Not ready for a call?
**Текст:**
> Score your team yourself first. The AI-Driven Modernization Readiness Checklist by Yevhen Kuzminov takes about [CONFIRM: 10] minutes and covers the same ground as the review.

**Посилання:** `Get the checklist →`

---

## 9. Фінальний CTA

`[VISUAL: темна секція (--black), по центру]`

**H2:** Find out where AI slows your releases
**Текст:**
> [CONFIRM: We run N reviews a week, so slots fill up.] 20 seconds for the form, [CONFIRM: 30] minutes on the call.

**Кнопка:** `Book my free review` (скрол до форми в hero)

---

## Технічний шар

- **Індексація.** Сторінка для трафіку з Shorts. Рекомендую `noindex`, щоб вона не конкурувала з основною сервісною сторінкою про AI SDLC / модернізацію. Якщо хочете органіку, потрібне окреме рішення про її місце в структурі сайту (parent, URL, внутрішні посилання), і тоді `noindex` знімаємо.
- **Навігація.** Прибрати меню хедера або залишити тільки лого. У футері тільки legal-посилання.
- **Sticky CTA на мобільному:** кнопка `Book my free review` внизу екрана, з'являється після hero.
- **Розподіл на архітектора:** приховане поле `architect` = `utm_content`; ліди з ним ідуть у календар цієї людини.
- **Персоналізація:** `utm_content` з кожного Short підставляє eyebrow, фото й ім'я в картку спікера. Те саме значення пишемо в приховане поле форми, щоб sales бачили, з якого ролика прийшов лід.
- **Події аналітики:** `form_view`, `form_start` (перший фокус), `form_submit`, `checklist_click`, `faq_open`, `sticky_cta_click`. Перевірити руками в GA4 DebugView перед запуском.
- **Schema:** `Service` (provider MobiDev, `offers.price: 0`) + `FAQPage`.
- **Зображення:** фото архітекторів і обкладинку чекліста у WebP до 200 KB, lazy-load нижче першого екрана.
- **Контраст:** білий текст на бірюзовій частині банера чекліста має бути ліворуч, де фон темний (#0a1f1a → #0d4f48). Праворуч, на #12B292, тексту не ставити.

## Що змінилося відносно поточної сторінки

| Було | Стало | Навіщо |
|---|---|---|
| «Free AI SDLC Readiness Discovery» | Заголовок з результатом: де AI гальмує delivery | Холодний глядач Shorts одразу розуміє, що отримає |
| Немає зв'язку з відео | Eyebrow + картка спікера за `utm_content` | Людина бачить того, кого щойно дивилася |
| 5 обов'язкових полів, одне текстове | 3 обов'язкових + 1 необов'язкове, решта після сабміту | Менше тертя на мобільному |
| Кнопка «Get my AI readiness level» | «Book my free review» + пояснення під кнопкою | Обіцянка збігається з тим, що реально станеться |
| Немає соцдоказів біля форми | Trust strip одразу під hero | Довіра до того, як людина вирішує |
| «9.1 NPS» | Виправлена метрика (треба підтвердити) | Неправильний NPS підриває довіру |
| Немає опису результату | Блок «What you leave with» + межа послуги | Людина знає, за що віддає 30 хвилин |
| Чекліст посередині | Чекліст у кінці | Не переманює лідів до того, як людина повірила |
| Немає FAQ і фінального CTA | FAQ з 7 питань + фінальний CTA | Знімає заперечення, дає другу точку конверсії |

## Оцінка сліпого судді (G-J, раунд 1)

Оцінював окремий агент, який не писав сторінку. Поріг 85/100.

| Вісь | Бал | Макс | Де втрачено |
|---|---|---|---|
| Conversion | 14 | 20 | події не перевірені; обіцянки часу розходилися (виправлено) |
| Offer clarity | 10 | 15 | тривалість дзвінка, склад score і SLA звіту не підтверджені |
| Structure | 10 | 15 | порожні слоти proof і досвіду експертів |
| Search and AI visibility | 7 | 15 | schema не валідована, noindex, FAQ без підтверджених відповідей |
| Human copy | 7 | 10 | «цитати» болів не дослівні (переписано в симптоми), кілька невдалих фраз (виправлено) |
| Proof | 3 | 10 | немає кейсу, цитати, джерел цифр |
| Design and UX | 4 | 10 | контраст, мобільний вигляд і клавіатура не перевірені |
| Technical layer | 1 | 5 | URL, canonical, швидкодія не визначені |
| **Разом** | **56** | **100** | із заповненими `[CONFIRM]` суддя прогнозує ~72 |

**Gate не пройдено: 56/85, найслабша вісь Proof.** Причина в даних, а не в тексті: ~20 `[CONFIRM]`, немає кейсу з цифрою і цитати клієнта, сторінку ще не зверстано і нічого не виміряно. Повторна оцінка без цих даних нічого не змінить.

Що підніме до 85: кейс з цифрою і цитата з Clutch (Proof), підтверджені тривалість дзвінка, склад score і SLA (Offer clarity), верстка з перевіркою контрасту й мобільного, валідована schema, перевірені події.
