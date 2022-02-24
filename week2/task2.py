import copy


def queue_time(customers_list: list, num_of_tills: int) -> int:
    stack = copy.copy(customers_list)
    tills = [stack.pop(0) for _ in range(num_of_tills) if stack]
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
    # tests
    assert queue_time([5, 3, 4], 1) == 12
    assert queue_time([10, 2, 3, 3], 2) == 10
    assert queue_time([2, 3, 10], 2) == 12
    assert queue_time([0, 1, 7, 2], 2) == 7
    assert queue_time([0, 0, 0, 0], 5) == 0
    assert queue_time([10, 2, 5, 6], 4) == 10
    print("All tests passed")
