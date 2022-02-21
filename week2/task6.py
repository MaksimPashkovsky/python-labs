import random


def monte_carlo_pi(num_of_points: int):
    points_inside = 0
    for i in range(num_of_points):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            points_inside += 1
    return 4 * points_inside / num_of_points


if __name__ == '__main__':
    print(monte_carlo_pi(1_000_000))
