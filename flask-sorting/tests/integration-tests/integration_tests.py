import requests
from config import Config

HOST = Config.SERVER_HOST
PORT = Config.SERVER_PORT


def test_shaker_sort():
    sorting_endpoint_test('shaker-sort')


def test_insertion_sort():
    sorting_endpoint_test('insertion-sort')


def test_selection_sort():
    sorting_endpoint_test('selection-sort')


def test_heap_sort():
    sorting_endpoint_test('heap-sort')


def sorting_endpoint_test(sorting_endpoint: str):
    data = [1, 3, 6, 8, 1, 2, 0, 0, 0]
    single_data_test(data, sorting_endpoint)

    data = [3, 36, -9, 26, 85, -26, 78, -82, 8, 60]
    single_data_test(data, sorting_endpoint)

    data = [3.0, 36.23, -9.102, 26.002, 85.3, -26.4, 78.909, -82, 8.1, 60.22]
    single_data_test(data, sorting_endpoint)

    data = []
    single_data_test(data, sorting_endpoint)

    requests.get(f'http://{HOST}:{PORT}/clear_all')


def single_data_test(data: list, sorting_endpoint: str):
    response = requests.post(f'http://{HOST}:{PORT}/{sorting_endpoint}', json=data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['time'] > 0
    assert response_json['sorted_list'] == sorted(data)
