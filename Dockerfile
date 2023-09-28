FROM python:3.10-slim-buster

WORKDIR /src

COPY __init__.py /src
COPY app.py /src
COPY config.py /src
COPY requirements.txt /src


RUN pip install -r requirements.txt

