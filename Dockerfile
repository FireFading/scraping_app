# pull the official base image
FROM python:3.10-alpine

WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]