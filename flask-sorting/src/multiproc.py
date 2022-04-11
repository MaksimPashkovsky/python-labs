from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from sorting import sort_with_time_measurement
from typing import Callable

process_pool = ProcessPoolExecutor()
thread_pool = ThreadPoolExecutor()


def sort_multiproc(data: list, sorting_function: Callable) -> dict:
    future = process_pool.submit(sort_with_time_measurement, data, sorting_function)
    res = future.result()
    return res
