FROM python:2.7.11-alpine

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN apk add --no-cache g++
RUN pip install -r requirements.txt
RUN python manage.py migrate

COPY . /src

CMD python manage.py runserver
