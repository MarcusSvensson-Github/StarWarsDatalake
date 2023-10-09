FROM python:3.12

RUN pip install pandas

RUN pip install requests

WORKDIR /app

COPY . /app

CMD python3 ingestion.py

