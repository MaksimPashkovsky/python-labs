import random
import multiprocessing
from week2.task6 import monte_carlo_pi as monte_carlo_pi_usual
from week3.task4 import ElapsedTimeMeasurer


def monte_carlo_pi(queue: multiprocessing.Queue):
    num_of_points = queue.get()
    points_inside = 0
    for i in range(num_of_points):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            points_inside += 1
    queue.put(points_inside)


def monte_carlo_pi_multiproc(num_of_points: int, num_of_processes: int):
    q = multiprocessing.Queue()

    for _ in range(num_of_processes):
        q.put(num_of_points // num_of_processes)

    procs = []

    for _ in range(num_of_processes):
        p = multiprocessing.Process(target=monte_carlo_pi, args=(q,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    total_point_inside = sum(q.get() for _ in range(num_of_processes))
    return 4 * total_point_inside / num_of_points


if __name__ == '__main__':
    points_number = 25_000_000
    with ElapsedTimeMeasurer() as etm1:
        print(monte_carlo_pi_usual(points_number))
    with ElapsedTimeMeasurer() as etm2:
        print(monte_carlo_pi_multiproc(points_number, 3))
    print(etm1.total_time, etm2.total_time)
