import requests
import threading
import multiprocessing
from flask import Flask, jsonify, request

app = Flask(__name__)

addresses_with_messages = dict()

messages = {1: 'Informational',
            2: 'Successful',
            3: 'Redirection',
            4: 'Client error',
            5: 'Server error'}


def do_request(url: str) -> tuple[str, str]:
    try:
        response = requests.head(url)
        if response.status_code == 405:
            response = requests.get(url)
        mes = messages[response.status_code // 100]
    except requests.exceptions.SSLError:
        mes = 'Connection refused'

    addresses_with_messages[url] = mes
    return url, mes


@app.route('/one_by_one', methods=['POST'])
def one_by_one():
    urls_str = request.form['list']
    urls = urls_str.replace(' ', '').split(',')

    for url in urls:
        do_request(url)

    return jsonify(addresses_with_messages)


@app.route('/threading', methods=['POST'])
def threads():

    urls_str = request.form['list']
    urls = urls_str.replace(' ', '').split(',')

    threads = []

    for url in urls:
        thread = threading.Thread(target=do_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return jsonify(addresses_with_messages)


@app.route('/multiprocessing', methods=['POST'])
def multiproc():
    urls_str = request.form['list']
    urls = urls_str.replace(' ', '').split(',')

    with multiprocessing.Pool(3) as pool:
        a = pool.map(do_request, urls)

    return jsonify(dict(a))


if __name__ == '__main__':
    app.run(host='localhost', port=8080)