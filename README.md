# Pipeline
https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines
[![Pipeline Status](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines)

# Создание виртуального окружения
+ Linux/macOS

```bash
python3 -m venv venv
```

+ Windows
```bash
python -m venv venv
```

# Активация
+ Linux/macOS

```bash
source venv/bin/activate
```

+ Windows
```bash
venv\Scripts\activate
```

Hello world!
Hello tutors!
python3 -m venv venv виртуалка
source venv/bin/activate линукс
venv\\Scripts\\activate винда
# Скачивание библиотек
```bash
pip freeze > requirements.txt
pip install -r requirements/dev.txt
pip install -r requirements/prod.txt
pip install -r requirements/test.txt
```
# Работа с .env
```bash
cp .env.example .env
```
Копирование из .env.example примера в .env

# Запуск приложения в dev режиме
Переходим в папку, в которой есть manage.py и запускаем
+ Linux/macOS
```bash
python3 manage.py runserver
```
+ Windows
```bash
python manage.py runserver
```