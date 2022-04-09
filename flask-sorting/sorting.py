import time
from typing import Callable
from heapq import heappush, heappop
from timer import ElapsedTimeMeasurer


def sort_with_time_measurement(data: list, sorting_function: Callable) -> dict:
    with ElapsedTimeMeasurer() as etm:
        sorted_data = sorting_function(data)
    return {'time': etm.total_time, 'sorted_list': sorted_data}


def shaker_sort(data: list) -> list:
    up = range(len(data) - 1)
    while True:
        for indexes in (up, reversed(up)):
            swapped = False
            for i in indexes:
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
            if not swapped:
                return data


def insertion_sort(data: list) -> list:
    for i in range(len(data)):
        j = i - 1
        temp = data[i]
        while data[j] > temp and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data


def selection_sort(data: list) -> list:
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data


def heap_sort(data: list) -> list:
    h = []
    for value in data:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


def measure_time(function):
    def wrapper(data):
        start = time.time()
        function(data)
        end = time.time()
        print(f"Time for sorting {len(data)} elements with {function.__name__}:", end - start)
    return wrapper