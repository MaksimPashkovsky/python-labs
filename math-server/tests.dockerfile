FROM python:3.10 AS base

RUN mkdir -p /usr/src/math-server

RUN mkdir -p /usr/src/math-server/tests
COPY src/mathserver/calc.py /usr/src/math-server/
COPY src/mathserver/operators.py /usr/src/math-server/

FROM base as unit-tests


COPY src/mathserver/tests/unit_tests.py /usr/src/math-server/tests/

WORKDIR /usr/src

CMD ["python", "-m", "math-server.tests.unit_tests"]