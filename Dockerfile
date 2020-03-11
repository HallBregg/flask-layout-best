FROM python:3.8
RUN apt-get update && apt-get -y upgrade

WORKDIR /tmp
COPY ./pocket/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /pocket
COPY ./pocket ./pocket

ENV PYTHONPATH="/"
ENV FLASK_APP='app.py'
EXPOSE 5000
