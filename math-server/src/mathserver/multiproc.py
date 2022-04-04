import multiprocessing
from .calc import do_calculation


def do_multiproc(data):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=do_calculation, args=(data, q))
    p.start()
    p.join()
    en, num1, num2, result = q.get()
    return en, num1, num2, result
