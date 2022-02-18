def lev(s: str, t: str):
    matrix = [
        [i + j if i * j == 0 else 0 for j in range(len(t) + 1)]
        for i in range(len(s) + 1)
    ]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(
                                matrix[i - 1][j],    # удаление
                                matrix[i][j - 1],    # вставка
                                matrix[i - 1][j - 1] # замена
                )
    print(*matrix, sep="\n")
    return matrix[len(s)][len(t)]


print(lev("kitten", "sitting"))