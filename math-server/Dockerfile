FROM python:3.10 AS base

RUN mkdir -p /usr/src/math-server

COPY src/mathserver /usr/src/math-server
COPY requirements.txt /usr/src/math-server

WORKDIR /usr/src/math-server

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS http-server

ENV HTTP_PORT=9000

EXPOSE 9000

FROM base AS socket-server

ENV SOCKET_PORT=8000

EXPOSE 8000
