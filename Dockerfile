FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

RUN adduser -D user
USER user