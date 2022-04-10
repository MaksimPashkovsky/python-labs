import orjson
import os
from hashing import hash_list
from flask import Flask, request
from typing import Callable
from sorting import shaker_sort, selection_sort, insertion_sort, heap_sort
from multiproc import sort_multiproc
from database import MongodbService
from config import Config

app = Flask(__name__)

storage = MongodbService.get_instance()


@app.route('/shaker-sort', methods=['POST'])
def shaker():
    return handle_sort(shaker_sort)


@app.route('/heap-sort', methods=['POST'])
def heap():
    return handle_sort(heap_sort)


@app.route('/selection-sort', methods=['POST'])
def selection():
    return handle_sort(selection_sort)


@app.route('/insertion-sort', methods=['POST'])
def insertion():
    return handle_sort(insertion_sort)


@app.route('/get_all_lists', methods=['GET'])
def get_all():
    res = storage.get_all()
    return orjson.dumps(res, default=str)


@app.route('/clear_all', methods=['GET'])
def clear():
    storage.clear_all()
    return "cleared"


def handle_sort(sorting_function: Callable):
    data = request.get_json()
    h = hash_list(data)

    if storage.has_hash(h):
        sorted_list = storage.get_by_hash(h)['sorted_list']
        return orjson.dumps({'time': 0, 'sorted_list': sorted_list})

    result = sort_multiproc(data, sorting_function)
    storage.save_data({
        'hash': h,
        'sorted_list': result['sorted_list']
    })
    return orjson.dumps(result)


if __name__ == '__main__':
    HOST = Config.SERVER_HOST
    PORT = Config.SERVER_PORT
    WORKER_PROCESSES = Config.WORKER_PROCESSES
    os.system(f"gunicorn -w {WORKER_PROCESSES} -b {HOST}:{PORT} main_app:app")