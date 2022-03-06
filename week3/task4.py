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


if __name__ == '__main__':
    with ElapsedTimeMeasurer() as etm:
        a = [i**100 for i in range(1_000_000)]
    print("Total time:", etm.total_time)
