def knapsack(total_weight, items, limit):
    K = [[0 for x in range(total_weight + 1)] for x in range(len(items) + 1)]

    for i in range(len(items) + 1):
        for j in range(total_weight + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif items[i - 1][0] <= j:  # does it fit?
                K[i][j] = max(items[i - 1][1] + K[i - 1][j - items[i - 1][0]],  # put item
                              K[i - 1][j])  # don't put item
            else:
                K[i][j] = K[i - 1][j]  # don't put item (doesn't fit)
    maximum = max(
        {K[i][j] for i in range(len(items) + 1) for j in range(total_weight + 1) if K[i][j] <= limit}
    )
    coords = [(i, j) for i in range(len(items) + 1) for j in range(total_weight + 1) if K[i][j] == maximum]
    i, j = coords[0]
    it = []
    while K[i][j]:
        if K[i][j] != K[i - 1][j]:
            it.append(items[i - 1])
            j = j - items[i - 1][0]
        i = i - 1
    return it


if __name__ == '__main__':
    # item is tuple (weight, price)
    itms = [(7, 10), (3, 4), (1, 2), (5, 6), (4, 7)]
    max_weight = 12
    money_limit = 17
    res = knapsack(max_weight, itms, money_limit)
    for w, c in res:
        print(f"Item: weight = {w}, cost = {c}")
    total_weight, total_sum = sum(list(zip(*res))[0]), sum(list(zip(*res))[1])
    print(f"Total weight = {total_weight}, total sum = {total_sum}")
