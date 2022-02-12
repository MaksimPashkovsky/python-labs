import math


def movie(card: int, ticket: int, perc: float):
    i = 1
    while True:
        sys_a_sum = i * ticket
        sys_b_sum = card + sum([ticket * (pow(perc, j)) for j in range(1, i + 1)])
        if math.ceil(sys_b_sum) < sys_a_sum:
            return i
        i += 1


print(movie(500, 15, 0.9))
