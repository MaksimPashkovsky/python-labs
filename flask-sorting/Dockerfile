FROM python:3.10 AS base

RUN mkdir -p /usr/src/flask-sorting

COPY src/. /usr/src/flask-sorting/
COPY requirements.txt /usr/src/flask-sorting/

WORKDIR /usr/src/flask-sorting

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main_app.py"]