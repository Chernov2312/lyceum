# Hello tutors!
## Lyceum Project
### Pipeline
[![flake8](https://img.shields.io/badge/flake8-passing-brightgreen)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main&job_name=flake8)
[![black](https://img.shields.io/badge/black-passing-brightgreen)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main&job_name=black)
[![tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines?scope=jobs&ref=main&job_name=django_test)

### Это учебный проект для специализации по django 
### Необходимое ПО
+ Python 3.13
+ git

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
+ Linux/macOS
```bash
cp .env.example .env
```

+ Windows
```bash
copy .env.example .env
```
Копирование из .env.example примера в .env

### Запуск приложения в dev режиме
Переходим в папку, в которой есть manage.py и запускаем
```bash
cd lyceum
```
+ Linux/macOS
```bash
python3 manage.py runserver
```
+ Windows
```bash
python manage.py runserver
```

### Ссылка где доступен сайт
+ http://127.0.0.1:8000/

### Запуск тестов
Переходим в папку lyceum если ещё не в ней
```bash
cd lyceum
```
Запускаем
+ Linux/macOS
```bash
python3 manage.py test
```
+ Windows
```bash
python manage.py test
```