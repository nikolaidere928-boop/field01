# Как новичку начать публиковать Field 01

Этот документ объясняет, что делать после подготовки файлов проекта. Он написан для ситуации, когда автор один, без академической сети и без опыта публичного научного продвижения.

Главная цель первого месяца — не доказать Field 01, а получить первые полезные замечания и не испортить впечатление чрезмерными заявлениями.

## 1. Перед публикацией

Перед тем как что-либо постить, проверь, что в проекте есть:

- `README.md`
- `FIELD01_OVERVIEW_EN.md`
- `CONTRIBUTING.md`
- `RELEASE_CHECKLIST.md`
- `FIRST_PUBLIC_POSTS.md`
- `articles/field01_formalization_program_en.tex`
- PDF основной статьи, если хочешь давать людям удобный файл для чтения.

Также проверь:

- нет личных файлов в публичной папке;
- нет случайных загрузок из `uploads/` или `prism-uploads/`;
- нет громких заявлений вроде “новая теория всего”;
- README прямо говорит, что это не завершённая теория.

## 2. Где лучше начать

Не начинай с arXiv.

Лучший порядок:

1. GitHub или GitLab — как публичный архив проекта.
2. Один маленький пост на Reddit с узким вопросом.
3. Несколько дней ожидания и спокойные ответы.
4. Исправление документов по критике.
5. Второй пост, уже по другой узкой теме.

## 3. Как создать GitHub-репозиторий

Общий порядок:

1. Зарегистрируйся или войди на GitHub.
2. Создай новый repository.
3. Назови его спокойно, например:

```text
field01
```

или:

```text
field01-formalization
```

4. Описание репозитория:

```text
Independent toy-level formalization project on phase circulation, closed nodes, memory, and boundary recording.
```

5. Сделай repository public только когда уверен, что личных файлов там нет.
6. Загрузи файлы проекта.
7. Убедись, что главная страница показывает `README.md`.

## 4. Что написать в описании GitHub

Короткое описание:

```text
Field 01 is an independent toy-level formalization project exploring phase circulation, closed nodes, scalar modulus / VEV-profile language with a normal-retention interpretation, memory classes, and boundary recording. It is not a completed physical theory; the project seeks criticism and comparison with established physics.
```

Не пиши:

```text
New theory of everything
```

```text
Replacement for modern physics
```

```text
Proof that black holes do not evaporate
```

## 5. Первый release на GitHub

Когда репозиторий готов, создай release:

Tag:

```text
v0.2-feedback
```

Title:

```text
Field 01 v0.2-feedback: cautious working archive after terminology cleanup
```

Description:

```text
This feedback checkpoint makes the Field 01 working archive inspectable after terminology cleanup. Field 01 is not presented as a completed physical theory. The release contains overview documents, contribution guidelines, working papers, roadmap material, and toy-model notes. The main purpose is to invite technical criticism, identify overlap with known physics, and clarify what must be formalized next.
```

## 6. Как начать на Reddit

На Reddit лучше не публиковать “всю теорию”.

Правило:

```text
Один пост = один узкий вопрос.
```

Начни с самого безопасного поста: вопроса о тоне и терминологии.

Подходящие сообщества:

- `r/AskPhysics`
- `r/PhysicsStudents`
- `r/AskAcademia`
- `r/PhilosophyofScience`

Но перед постом обязательно прочитай правила каждого subreddit. Некоторые запрещают личные теории или саморекламу.

## 7. Первый пост на Reddit

Лучший первый пост — не про “модель”, а про то, как её правильно подавать.

Возьми текст из `FIRST_PUBLIC_POSTS.md`, раздел:

```text
Post 2 — Terminology and Scientific Tone
```

Почему он лучше для старта:

- он не выглядит как попытка доказать новую физику;
- он показывает осторожность;
- он может дать советы по языку;
- он снижает риск агрессивной реакции.

## 8. Когда давать ссылку

Не ставь ссылку сразу в каждый пост, если subreddit этого не любит.

Лучше так:

1. Написать вопрос без ссылки.
2. Если кто-то попросит контекст, дать ссылку на `FIELD01_OVERVIEW_EN.md`.
3. Не давать сразу книгу.
4. Не давать сразу 10 файлов.

Если ссылка разрешена, добавляй только одну:

```text
For context, here is the short overview: [link]
```

## 9. Как отвечать на критику

Не спорь сразу.

Хороший ответ:

```text
Thank you — this is useful. I am trying to identify exactly where the project overlaps with known physics and where the language should be weakened. I will revise the overview accordingly.
```

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

## 10. Чего не делать

Не делай этого:

- не публикуй книгу целиком первым сообщением;
- не пиши “я доказал”;
- не спорь с людьми, которые знают стандартную физику лучше;
- не проси arXiv endorsement у незнакомцев;
- не пость одно и то же в 10 subreddit подряд;
- не воспринимай критику как личное нападение;
- не отвечай длинными философскими текстами на короткие технические замечания.

## 11. Что считать успехом

Успех первого месяца — это не популярность.

Успех:

- один человек дал полезную ссылку;
- один человек указал на ошибку;
- один термин стал понятнее;
- один абзац стал осторожнее;
- проект стал менее уязвимым.

Даже жёсткая критика может быть полезной, если из неё понятно, что исправить.

## 12. Порядок действий на первую неделю

День 1:

- проверить `README.md`;
- проверить `FIELD01_OVERVIEW_EN.md`;
- проверить, что нет личных файлов.

День 2:

- создать GitHub/GitLab repository;
- загрузить проект;
- проверить, как выглядит главная страница.

День 3:

- создать или обновить release `v0.2-feedback`;
- сохранить ссылку на repository.

День 4:

- выбрать один subreddit;
- прочитать правила;
- подготовить первый пост без лишних ссылок.

День 5:

- опубликовать первый пост;
- не спорить;
- сохранить все полезные замечания.

День 6–7:

- внести правки в overview;
- записать feedback log;
- не публиковать второй пост слишком быстро.

## 13. Минимальный feedback log

Создай файл или таблицу с колонками:

```text
Date | Place | Comment | Problem Type | My Response | Action | Status
```

Пример:

```text
2026-06-04 | Reddit | Similar to Abelian-Higgs vortex | literature overlap | thanked user | add reference/comparison | open
```

## 14. Главная стратегия

Тебе не нужно сразу попасть в “большую науку”.

Тебе нужно сделать так, чтобы проект выглядел:

- честным;
- аккуратным;
- открытым к критике;
- технически проверяемым;
- не агрессивным к существующей физике.

Для независимого автора это лучший путь к доверию.