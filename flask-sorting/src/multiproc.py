from concurrent.futures import ProcessPoolExecutor
from sorting import sort_with_time_measurement
from typing import Callable

executor = ProcessPoolExecutor()


def sort_multiproc(data: list, sorting_function: Callable) -> dict:
    future = executor.submit(sort_with_time_measurement, data, sorting_function)
    res = future.result()
    return res
