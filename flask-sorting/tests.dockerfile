FROM python:3.10 AS base

RUN mkdir -p /usr/src/flask-sorting

FROM base AS unit-tests

COPY tests/unit_tests.py /usr/src/flask-sorting/
COPY src/hashing.py /usr/src/flask-sorting/
COPY src/sorting.py /usr/src/flask-sorting/

WORKDIR /usr/src/flask-sorting

CMD ["python", "unit_tests.py"]