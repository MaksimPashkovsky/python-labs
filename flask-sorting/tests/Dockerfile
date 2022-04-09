FROM python:3.10 AS base

RUN mkdir -p /usr/src/flask-sorting

WORKDIR /usr/src/flask-sorting

FROM base AS unit-tests

COPY tests/unit_tests.py /usr/src/flask-sorting/
COPY src/hashing.py /usr/src/flask-sorting/
COPY src/sorting.py /usr/src/flask-sorting/

CMD ["python", "unit_tests.py"]

FROM base AS integration-tests

COPY tests/integration_tests.py /usr/src/flask-sorting/
COPY tests/tests-requirements.txt /usr/src/flask-sorting/

RUN pip install --no-cache-dir -r tests-requirements.txt

CMD ["pytest", "integration_tests.py"]