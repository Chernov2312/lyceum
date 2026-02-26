# Hello tutors!
## Lyceum Project
### Pipeline
[![flake8](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/badges/main/pipeline.svg?job=flake8&key_text=flake8)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main)

[![black](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/badges/main/pipeline.svg?job=black&key_text=black)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main)

[![tests](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/badges/main/pipeline.svg?job=django_test&key_text=tests)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main)


### Это учебный проект для специализации по django 
### Необходимое ПО
+ Python 3.13
https://www.python.org/downloads/
+ git
ссылка
https://github.com/apps/desktop
### Скопировать git репозиторий
```bash
git clone https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585
```

### Переход в скопированную директорию
```bash
cd 173126-m.chernov.tchernov-course-1585
```
### Создание виртуального окружения
+ Linux/macOS

```bash
python3 -m venv venv
```

+ Windows
```bash
python -m venv venv
```

### Активация
+ Linux/macOS

```bash
source venv/bin/activate
```

+ Windows
```bash
venv\Scripts\activate
```

### Скачивание библиотек
```bash
pip install -r requirements/dev.txt
pip install -r requirements/prod.txt
pip install -r requirements/test.txt
```
### Работа с .env
```bash
cp .env.example .env
```
Копирование из .env.example примера в .env
### Настройка локализации
Переходим в папку lyceum
```bash
cd lyceum
```
В папке lyceum вводим команду с языком который нам нужен
```bash
django-admin makemessages --all
```
В папке locale в файлах django.po заполняем перевод по типу
```bash
msgid "балтики"
msgstr "Baltika beers"
```
Применить перевод
```bash
django-admin compilemessages -l <язык>
```
В файле settings.py 
LANGUAGE_CODE = 'ru' отвечает за язык разработки
Также добавляем в качестве поддерживаемых языков приложения
```bash
LANGUAGES = [
    ("ru", "Русский"),
    ("en", "English"),
    ("de", "Deutsch"),
]
```
### Создание superuser
Переходим в папку lyceum если ещё не в ней
```bash
cd lyceum
```
Создаём
```
python manage.py createsuperuser
```
### Запуск приложения в dev режиме
Переходим в папку lyceum если ещё не в ней
```bash
cd lyceum
```
```bash
python3 manage.py runserver
```

### Ссылка где доступен сайт
+ http://127.0.0.1:8000/

### Запуск тестов
Переходим в папку lyceum если ещё не в ней
```bash
cd lyceum
```
Запускаем
```bash
python3 manage.py test
```
# Подвал
### ER база данных
![ER-диаграмма проекта](ER.jpg)