FROM python:3.10 AS base

RUN mkdir -p /usr/src/math-server

# Copying common files
COPY requirements.txt /usr/src/math-server
COPY src/mathserver/operators.py /usr/src/math-server/
COPY src/mathserver/models.py /usr/src/math-server/

WORKDIR /usr/src/math-server

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS http-server

RUN mkdir -p /usr/src/math-server/servers
COPY src/mathserver/servers/flask_server.py /usr/src/math-server/servers/
COPY src/mathserver/calc.py /usr/src/math-server/
COPY src/mathserver/db_setup.py /usr/src/math-server/

WORKDIR /usr/src

CMD ["python", "-m", "math-server.servers.flask_server"]

FROM base AS socket-server

RUN mkdir -p /usr/src/math-server/servers
COPY src/mathserver/servers/socket_server.py /usr/src/math-server/servers/
COPY src/mathserver/calc.py /usr/src/math-server/
COPY src/mathserver/db_setup.py /usr/src/math-server/

WORKDIR /usr/src

CMD ["python", "-m", "math-server.servers.socket_server"]

FROM base AS migrations

RUN mkdir -p /usr/src/math-server/alembic
COPY migrations/. /usr/src/math-server/
# COPY migrations/alembic.ini /usr/src/math-server/

CMD ["alembic", "upgrade", "head"]