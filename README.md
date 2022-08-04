## before start you need to create virtual env: $ python3 -m venv venv & source ./venv/bin/activate & pip -r install requirements.txt
## to start rabbitmq: $ brew services start rabbitmq
## to start django app: $ python manage.py runserver
## to start celery: $ celery worker -B -l INFO