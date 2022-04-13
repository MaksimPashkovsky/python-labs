from time import perf_counter


class ElapsedTimeMeasurer:

    def __init__(self):
        self.__start = None
        self.total_time = None

    def __enter__(self):
        self.__start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total_time = perf_counter() - self.__start
