def lev(s: str, t: str, *,
        insertion_cost: float = 0.5,
        deletion_cost: float = 0.5,
        replacement_cost: float = 1.0,
        print_matrix = 0,
        tab_size = 5,
        print_detailed_result = 0):
    """
    Returns Levenshtein distance from string s to string t
    To print transformation matrix change the value of print_matrix argument
    To display detailed result with all steps of transformation change the print_detailed_result argument
    """
    matrix = [
        [float(i + j) if i * j == 0 else 0 for j in range(len(t) + 1)]
        for i in range(len(s) + 1)
    ]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                minimal = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                matrix[i][j] = deletion_cost + matrix[i - 1][j] if matrix[i - 1][j] == minimal \
                    else insertion_cost + matrix[i][j - 1] if matrix[i][j - 1] == minimal \
                    else replacement_cost + matrix[i - 1][j - 1]
    if print_matrix:
        print(("\t\t\t" + "\t".join(t)).expandtabs(tab_size))
        print(("\t\t\t" + "―\t" * len(t)).expandtabs(tab_size))
        print(("\t\t" + "\t".join([str(n) for n in matrix[0]])).expandtabs(tab_size))
        for i in range(1, len(matrix)):
            print((s[i - 1] + "\t" + "|\t" + "\t".join([str(n) for n in matrix[i]])).expandtabs(tab_size))

    if print_detailed_result:
        i, j = len(s), len(t)
        print(s, "->", t)
        current_minimal = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
        previous_minimal = matrix[len(s)][len(t)]
        temp = list(s)
        while previous_minimal != 0:
            if current_minimal == matrix[i][j - 1]:
                if previous_minimal != current_minimal:
                    temp.insert(i, t[j - 1])
                    print(f"{''.join(temp)} : Inserted '{t[j - 1]}', cost = {insertion_cost}")
                j = j - 1
            elif current_minimal == matrix[i - 1][j]:
                if previous_minimal != current_minimal:
                    temp.pop(j)
                    print(f"{''.join(temp)} : Deleted '{s[j]}', cost = {deletion_cost}")
                i = i - 1
            else:
                if previous_minimal != current_minimal:
                    tmp = temp[i - 1]
                    temp[i - 1] = t[j - 1]
                    print(f"{''.join(temp)} : Replaced '{tmp}' -> '{t[j - 1]}', cost = {replacement_cost}")
                i = i - 1
                j = j - 1

            previous_minimal = current_minimal
            current_minimal = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])

    return matrix[len(s)][len(t)]


print(lev("sitting", "kitten", print_matrix=1, print_detailed_result=1))
