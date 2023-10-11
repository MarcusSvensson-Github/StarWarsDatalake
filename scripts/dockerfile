FROM python:3.12

RUN pip install pandas

RUN pip install requests

RUN pip install sqlalchemy

RUN pip install psycopg2

WORKDIR /app

COPY . /app

CMD python3 ingestion.py

FROM jupyter/datascience-notebook:latest

WORKDIR /app

COPY . /app

RUN pip install pandas
