import re
from collections import Counter


def parse_molecule(molecule: str) -> dict:
    tokens = re.findall(r"[A-Z][a-z]?|\)|\]|\}|\(|\[|\{|\d+", molecule)
    # K4(ON(SO3)2)2 -> ['K', '4', '(', 'O', 'N', '(', 'S', 'O', '3', ')', '2', ')', '2']
    i = 0
    new_tokens = []
    while i < len(tokens):
        if tokens[i].isalpha() and i + 1 < len(tokens) and tokens[i + 1].isdigit():
            new_tokens += [tokens[i]] * int(tokens[i + 1])
            i += 1
        else:
            new_tokens.append(tokens[i])
        i += 1
    # ['K', '4', '(', 'O', 'N', '(', 'S', 'O', '3', ')', '2', ')', '2'] ->
    # ['K', 'K', 'K', 'K', '(', 'O', 'N', '(', 'S', 'O', 'O', 'O', ')', '2', ')', '2']
    while "(" in new_tokens or "{" in new_tokens or "[" in new_tokens:
        start, end, multiplier, j = 0, 0, 0, 0
        while j < len(new_tokens):
            if new_tokens[j] in "({[":
                start = j
            elif new_tokens[j] in ")}]":
                end = j
                multiplier = int(new_tokens[j + 1]) if j + 1 < len(new_tokens) and new_tokens[j + 1].isdigit() else 1
                break
            j += 1
        shift = 0 if multiplier == 1 else 1  # если после скобки нет числа, сдвигать не надо
        new_tokens = new_tokens[:start] + new_tokens[start + 1:end] * multiplier + new_tokens[end + 1 + shift:]
    # ['K', 'K', 'K', 'K', '(', 'O', 'N', '(', 'S', 'O', 'O', 'O', ')', '2', ')', '2'] ->
    # ['K', 'K', 'K', 'K', '(', 'O', 'N', 'S', 'O', 'O', 'O', 'S', 'O', 'O', 'O', ')', '2'] ->
    # ['K', 'K', 'K', 'K', 'O', 'N', 'S', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'O', 'N', 'S', 'O', 'O', 'O', 'S', 'O', 'O', 'O',]
    return dict(Counter(new_tokens))


print(parse_molecule("K4{ON[SO3]2}2"))
