import time


class ElapsedTimeMeasurer:

    def __enter__(self):
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total_time = time.time() - self.__start


if __name__ == '__main__':
    with ElapsedTimeMeasurer() as etm:
        a = [i**100 for i in range(1_000_000)]
    print("Total time:", etm.total_time)
