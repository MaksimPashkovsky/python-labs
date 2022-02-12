def first_last_words(string: str):
    words = string.lower().split(" ")
    return words[0].capitalize() + " ".join(words[1:-1]) + " " + words[-1].capitalize()


print(first_last_words(input()))
