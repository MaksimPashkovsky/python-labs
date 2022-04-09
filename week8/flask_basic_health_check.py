import requests
import multiprocessing
from multiprocessing.pool import ThreadPool
from flask import Flask, jsonify, request

app = Flask(__name__)

messages = {1: 'Informational',
            2: 'Successful',
            3: 'Redirection',
            4: 'Client error',
            5: 'Server error'}

THREAD_POOL = ThreadPool()
PROCESS_POOL = None


def do_request(url: str) -> tuple[str, str]:
    try:
        response = requests.head(url)
        if response.status_code == 405:
            response = requests.get(url)
        mes = messages[response.status_code // 100]
    except requests.exceptions.SSLError:
        mes = 'Connection refused'
    return url, mes


@app.route('/one_by_one', methods=['POST'])
def one_by_one():
    urls = request.get_json()
    d = dict(map(do_request, urls))
    return jsonify(d)


@app.route('/threading', methods=['POST'])
def threads():
    urls = request.get_json()
    res = THREAD_POOL.map(do_request, urls)
    return jsonify(dict(res))


@app.route('/multiprocessing', methods=['POST'])
def multiproc():
    urls = request.get_json()
    res = PROCESS_POOL.map(do_request, urls)
    return jsonify(dict(res))


if __name__ == '__main__':
    PROCESS_POOL = multiprocessing.Pool(4)
    app.run(host='localhost', port=8080)