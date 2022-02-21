import copy


def queue_time(customers_list: list, num_of_tills: int):
    stack = copy.copy(customers_list)
    tills = [stack.pop(0) for _ in range(num_of_tills)]
    counter = 0
    while stack:
        min_time = min(tills)
        i = tills.index(min_time)
        tills = [el - min_time for el in tills]
        tills[i] = stack.pop(0)
        counter += min_time
    return counter + max(tills)


if __name__ == '__main__':
    initial_queue = [2, 3, 10]
    num_of_tills = 3
    print(queue_time(initial_queue, num_of_tills))
