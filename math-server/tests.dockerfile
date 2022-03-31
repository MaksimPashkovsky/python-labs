FROM python:3.10 AS base

RUN mkdir -p /usr/src/math-server
RUN mkdir -p /usr/src/math-server/tests

FROM base as unit-tests

COPY src/mathserver/calc.py /usr/src/math-server/
COPY src/mathserver/operators.py /usr/src/math-server/
COPY tests/unit_tests.py /usr/src/math-server/tests/

WORKDIR /usr/src

CMD ["python", "-m", "math-server.tests.unit_tests"]

FROM base AS integration-tests

WORKDIR /usr/src/math-server

COPY test-requirements.txt /usr/src/math-server

RUN pip install --no-cache-dir -r test-requirements.txt

FROM integration-tests AS integration-tests-http

COPY tests/integration_tests_http.py /usr/src/math-server/tests/

CMD ["pytest", "tests/integration_tests_http.py"]

FROM integration-tests AS integration-tests-socket

COPY tests/integration_tests_socket.py /usr/src/math-server/tests/

CMD ["pytest", "-v", "tests/integration_tests_socket.py"]

FROM integration-tests AS migrations-tests

RUN mkdir -p /usr/src/math-server/alembic
COPY migrations/. /usr/src/math-server/
COPY src/mathserver/operators.py /usr/src/math-server/
COPY tests/migrations_tests.py /usr/src/math-server/

CMD ["pytest", "-v" , "migrations_tests.py"]