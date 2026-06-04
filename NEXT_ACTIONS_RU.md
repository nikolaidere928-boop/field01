# Следующие действия для публикации Field 01

Это короткая практическая инструкция: что делать руками, когда ты готов открыть проект наружу.

## 0. Главное правило

Не пытайся сразу “зайти в науку”.

Первый шаг — создать аккуратный публичный архив и задать один осторожный вопрос.

Твоя позиция:

```text
Я независимый автор. Это не завершённая теория. Я ищу критику, ссылки, проверку терминов и сравнение с известной физикой.
```

## 1. Создай репозиторий

Открой GitHub или GitLab и создай новый repository.

Название:

```text
field01-formalization
```

или короче:

```text
field01
```

Описание:

```text
Independent toy-level formalization project on phase circulation, closed nodes, memory, and boundary recording.
```

Visibility:

```text
Public
```

Но делай `Public` только после проверки, что туда не попадут личные файлы.

## 2. Загрузи сначала минимальный набор

Для первого публичного варианта загрузи эти файлы:

```text
README.md
FIELD01_OVERVIEW_EN.md
CONTRIBUTING.md
LICENSE_NOTE.md
PUBLIC_READY_STATUS.md
PUBLIC_FILE_MANIFEST.md
RELEASE_CHECKLIST.md
FIRST_PUBLIC_POSTS.md
BEGINNER_PUBLICATION_GUIDE_RU.md
FEEDBACK_LOG.md
FOUR_WEEK_LAUNCH_PLAN.md
PROJECT_ROADMAP_EN.md
OUTREACH_PACKAGE_EN.md
OUTREACH_LETTER_EN.md
ABSTRACTS_EN.md
FIELD01_GLOSSARY.md
```

Потом папку:

```text
articles/
```

Минимально из `articles/`:

```text
articles/field01_formalization_program_en.tex
articles/field01_formalization_program_en.pdf
articles/particle_as_closed_wave_en.tex
articles/horizon_as_phase_recording_surface_en.tex
```

Потом, если хочешь показать воспроизводимость:

```text
analysis/numerics/solve_phase_normal_profile.py
analysis/numerics/solve_screened_phase_normal_profile.py
```

## 3. Не загружай это

Не загружай:

```text
uploads/
prism-uploads/
AGENTS.md
.git/
```

Не загружай временные LaTeX-файлы:

```text
*.aux
*.log
*.out
*.fls
*.fdb_latexmk
*.synctex
```

## 4. Проверь главную страницу

После загрузки открой repository как обычный посетитель.

Проверь:

- видно ли `README.md` на главной странице;
- понятно ли за 1 минуту, что это не “новая теория всего”;
- есть ли ссылка на `FIELD01_OVERVIEW_EN.md`;
- есть ли ссылка на `CONTRIBUTING.md`;
- нет ли личных файлов.

## 5. Создай первый release

В GitHub открой:

```text
Releases -> Create a new release
```

Tag:

```text
v0.1-public
```

Title:

```text
Field 01 v0.1-public: cautious working archive for criticism
```

Description:

```text
This first public release makes the Field 01 working archive inspectable. Field 01 is not presented as a completed physical theory. The release contains overview documents, contribution guidelines, working papers, roadmap material, and toy-model notes. The main purpose is to invite technical criticism, identify overlap with known physics, and clarify what must be formalized next.
```

## 6. Подожди один день

Не беги сразу на Reddit.

Сначала на следующий день перечитай:

```text
README.md
FIELD01_OVERVIEW_EN.md
CONTRIBUTING.md
```

Если самому кажется, что где-то звучит слишком громко — ослабь формулировку.

## 7. Первый пост на Reddit

Первый пост лучше сделать не про теорию, а про тон и терминологию.

Используй файл:

```text
FIRST_PUBLIC_POSTS.md
```

Раздел:

```text
Post 2 — Terminology and Scientific Tone
```

Лучшие subreddit для первого осторожного поста:

```text
r/AskPhysics
r/PhysicsStudents
r/AskAcademia
```

Перед публикацией прочитай правила subreddit. Если там запрещены личные теории, не публикуй туда модель. Сформулируй вопрос как вопрос о научной подаче и терминологии.

## 8. Не давай ссылку сразу, если не уверен

Если правила subreddit неясны, первый пост сделай без ссылки.

Если кто-то попросит контекст, дай одну ссылку:

```text
FIELD01_OVERVIEW_EN.md
```

Не давай сразу книгу. Не давай сразу весь набор статей.

## 9. Как отвечать

Если говорят “это уже известно”:

```text
Thank you. That is exactly what I need to clarify. Could you point me to the closest standard reference so I can cite it and avoid claiming novelty there?
```

Если говорят “это слишком vague”:

```text
That is fair. Could you point to the first definition that becomes too vague to be useful? I am trying to decide what to formalize first.
```

Если отвечают грубо:

```text
I understand the concern. I am not asking for endorsement and I am not claiming a completed theory. I am trying to identify errors and overstatements.
```

## 10. После первого поста

Не публикуй второй пост сразу.

Сделай так:

1. Сохрани все полезные замечания в `FEEDBACK_LOG.md`.
2. Раздели замечания на типы: термин, уравнение, ссылка, overclaim, known overlap.
3. Исправь `FIELD01_OVERVIEW_EN.md`.
4. Если критика важная, исправь `README.md`.
5. Только потом думай о втором посте.

## 11. Второй пост

Второй пост лучше сделать техническим:

```text
FIRST_PUBLIC_POSTS.md -> Post 1 — Abelian-Higgs / Vortex Comparison
```

Его цель:

- понять, насколько модель совпадает с известными vortex/Abelian-Higgs структурами;
- получить ссылки;
- убрать ложную новизну;
- сделать статью сильнее.

## 12. Что считать хорошим результатом

Хороший результат — это не лайки.

Хороший результат:

- тебе дали 2–3 ссылки;
- указали на слабый термин;
- сказали, что похоже на конкретную известную модель;
- показали, где формулировка звучит слишком сильно;
- один человек попросил ссылку на overview.

## 13. Если будет тяжело психологически

Это нормально.

Независимому автору трудно выходить наружу, особенно с физикой. Не спорь с каждым. Твоя задача — не победить в комментариях, а улучшить проект.

Повторяй себе:

```text
Критика — это материал для v0.2-feedback.
```

## 14. Когда можно думать об arXiv

Не сейчас.

Думать об arXiv стоит только после:

- публичного repository;
- первой критики;
- версии `v0.2-feedback`;
- добавления ссылок на стандартную литературу;
- улучшения формализационной статьи;
- хотя бы одного внешнего человека, который сказал: “это можно оформить как препринт”.

## 15. Самый короткий план

Если совсем кратко:

1. Создай GitHub repository.
2. Загрузи public-ready файлы.
3. Создай release `v0.1-public`.
4. Подожди один день.
5. Сделай первый осторожный Reddit-пост про тон и терминологию.
6. Записывай критику в `FEEDBACK_LOG.md`.
7. Исправь overview.
8. Только потом делай технический пост про Abelian-Higgs/vortex comparison.