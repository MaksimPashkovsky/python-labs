import itertools


def count_ways(S, n):
    num_of_ways = [0 for _ in range(n + 1)]
    num_of_ways[0] = 1

    for i in range(len(S)):
        for j in range(S[i], n + 1):
            num_of_ways[j] += num_of_ways[j - S[i]]
    return num_of_ways[n]


def all_combinations(l, amount, n):
    res = []
    k, i = 0, 0
    while True:
        for c in itertools.combinations_with_replacement(l, r=i):
            if sum(c) == amount:
                res.append(c)
                k += 1
        if k == n:
            break
        i += 1
    return res


if __name__ == '__main__':
    bills = [1, 2, 5]
    amount = 10
    ways = count_ways(bills, amount)
    print(f"There are {ways} ways to pay {amount} using coins: " + ", ".join([str(b) for b in bills]))
    combs = all_combinations(bills, amount, ways)
    for el in combs:
        str_nums = [str(num) for num in el]
        print(f"{amount} = " + " + ".join(str_nums))