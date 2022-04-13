#!/bin/bash

gunicorn -w $WORKER_PROCESSES -b $SERVER_HOST:$SERVER_PORT main_app:app