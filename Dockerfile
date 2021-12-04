FROM python:3
WORKDIR /data

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt /data/
RUN pip install -r requirements.txt

COPY . /data/
RUN python manage.py makemigrations PluginBackend Web
RUN python manage.py migrate
RUN python manage.py loaddata PluginBackend/json/data.json