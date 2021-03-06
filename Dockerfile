FROM python:3.9-slim-buster
MAINTAINER Ali Ayar <gavaryus@gmail.com>

ENV INSTALL_PATH /snakeeyes
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "snakeeyes.app:create_app()"