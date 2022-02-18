import copy


def queue_time(customers_list: list, num_of_tills: int):
    stack = copy.copy(customers_list)
    tills = [stack.pop(0) for c in range(num_of_tills)]
    counter = 0
    while stack:
        min_time = min(tills)
        i = tills.index(min_time)
        tills = [el - min_time for el in tills]
        tills[i] = stack.pop(0)
        counter += min_time
    return counter + max(tills)


print(queue_time([2, 3, 10], 3))
