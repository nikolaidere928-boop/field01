# Как загрузить Field 01 на GitHub Desktop без ZIP

Используйте этот способ, если `field01_github_upload_package.zip` не появляется в Prism.

Главная готовая папка теперь называется:

```text
GITHUB_UPLOAD_READY
```

Именно её содержимое нужно копировать в GitHub Desktop.

## 1. Скачать проект из Prism

1. В левом верхнем углу Prism нажмите на название проекта:

```text
Universe as a Memory Wave (Model 01)
```

2. В выпадающем меню выберите:

```text
Export
```

3. Prism скачает архив всего проекта на компьютер.
4. Распакуйте этот архив в обычную папку.

## 2. Найти готовую папку для GitHub

Внутри распакованного проекта откройте папку:

```text
GITHUB_UPLOAD_READY
```

Это готовый набор файлов для GitHub.

Если такой папки почему-то нет, запасной вариант:

```text
public_release
```

Копировать нужно **содержимое** папки `GITHUB_UPLOAD_READY`, а не саму папку.

Внутри должны быть, например:

```text
README.md
FIELD01_GITHUB_START_HERE.md
CONTRIBUTING.md
PUBLIC_READY_STATUS.md
analysis/
articles/
```

## 3. Открыть папку GitHub Desktop

1. Откройте GitHub Desktop.
2. Убедитесь, что выбран репозиторий:

```text
field01
```

3. Нажмите кнопку:

```text
Show in Explorer
```

Откроется папка локального GitHub-репозитория.

## 4. Скопировать файлы

1. Вернитесь в распакованную папку `GITHUB_UPLOAD_READY`.
2. Выделите всё внутри `GITHUB_UPLOAD_READY`.
3. Скопируйте.
4. Вставьте в папку `field01`, которую открыл GitHub Desktop.
5. Если Windows спросит о замене файлов, выберите замену.

Правильно:

```text
GITHUB_UPLOAD_READY/README.md -> field01/README.md
GITHUB_UPLOAD_READY/FIELD01_GITHUB_START_HERE.md -> field01/FIELD01_GITHUB_START_HERE.md
```

Неправильно:

```text
field01/GITHUB_UPLOAD_READY/README.md
```

## 5. Сделать commit и push

В GitHub Desktop:

1. Слева появятся изменённые файлы.
2. В поле `Summary` напишите:

```text
Prepare public Field01 GitHub entrypoint
```

3. Нажмите:

```text
Commit to main
```

4. Потом нажмите:

```text
Push origin
```

## 6. Проверить на GitHub

Откройте страницу репозитория в браузере и проверьте, что в верхнем списке файлов появился файл:

```text
FIELD01_GITHUB_START_HERE.md
```

Если он появился, загрузка прошла успешно.

## 7. Если появится ошибка

Если GitHub Desktop покажет `conflict`, `rejected`, `authentication failed` или красную ошибку, ничего больше не нажимайте. Сделайте скрин и пришлите его в чат.