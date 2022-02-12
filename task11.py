def num_string(inp: list):
    temp = ['~'] * len(inp)
    try:
        for i, c in inp:
            temp[i] = c
        return "".join(temp)
    except (TypeError, ValueError, IndexError):
        return False


print(num_string([(4, 'y'), (1, 'o'), (0, 'm'), (2, 'n'), (3, 't')]))
