import random
import multiprocessing
from week2.task6 import monte_carlo_pi as monte_carlo_pi_usual
from week3.task4 import ElapsedTimeMeasurer


def monte_carlo_pi_partial(num_of_points):
    points_inside = 0
    for i in range(num_of_points):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            points_inside += 1
    return points_inside


def monte_carlo_pi_multiproc(num_of_points: int):

    with multiprocessing.Pool() as pool:
        res = pool.map(monte_carlo_pi_partial, [num_of_points // 4] * 4)

    total_point_inside = sum(res)
    return 4 * total_point_inside / num_of_points


if __name__ == '__main__':
    points_number = 30_000_000
    with ElapsedTimeMeasurer() as etm1:
        print(monte_carlo_pi_usual(points_number))
    with ElapsedTimeMeasurer() as etm2:
        print(monte_carlo_pi_multiproc(points_number))
    print(etm1.total_time, etm2.total_time)
