# Как загрузить Field 01 на GitHub Desktop без ZIP

Используйте этот способ, если `field01_github_upload_package.zip` не появляется в Prism.

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

## 2. Найти готовую публичную папку

Внутри распакованного проекта откройте папку:

```text
public_release
```

Это готовый набор файлов для GitHub. Копировать нужно **содержимое** этой папки, а не саму папку `public_release`.

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

1. Вернитесь в распакованную папку `public_release`.
2. Выделите всё внутри `public_release`.
3. Скопируйте.
4. Вставьте в папку `field01`, которую открыл GitHub Desktop.
5. Если Windows спросит о замене файлов, выберите замену.

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

Откройте страницу репозитория в браузере и проверьте, что появился файл:

```text
FIELD01_GITHUB_START_HERE.md
```

Если он появился, загрузка прошла успешно.

## 7. Если появится ошибка

Если GitHub Desktop покажет `conflict`, `rejected`, `authentication failed` или красную ошибку, ничего больше не нажимайте. Сделайте скрин и пришлите его в чат.