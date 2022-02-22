import random


def monte_carlo_pi(num_of_points: int) -> float:
    points_inside = 0
    for i in range(num_of_points):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            points_inside += 1
    return 4 * points_inside / num_of_points


def monte_carlo_pi2(num_of_points: int) -> float:
    return 4 * sum(
        1 for _ in range(num_of_points) if random.random() ** 2 + random.random() ** 2 <= 1
    ) / num_of_points


if __name__ == '__main__':
    print(monte_carlo_pi(1_000_000))
    # one line solution is a little slower
    print(monte_carlo_pi2(1_000_000))
