from .calc import do_calculation
from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor(4)


def do_multiproc(data):
    fut = executor.submit(do_calculation, data)
    return fut.result()
