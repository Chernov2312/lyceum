https://gitlab.crja72.ru/django/2026/spring/course/students/173126-m.chernov.tchernov-course-1585/-/pipelines
Hello world!
Hello tutors!
python3 -m venv venv виртуалка
source venv/bin/activate линукс
venv\\Scripts\\activate винда
pip freeze > requirements.txt
pip install -r requirements/dev.txt
pip install -r requirements/prod.txt
pip install -r requirements/test.txt
cp .env.example .env копирование из .env.example примера в .env
Переходим с помощью команды cd в папку где есть manage.py, после пишем команду для запуска dev режима"python3 manage.py runserver"(если windows то "python manage.py runserver"), на запуск в dev режиме влияет переменная debug из файла settings, по умолчанию True(dev режим включен)