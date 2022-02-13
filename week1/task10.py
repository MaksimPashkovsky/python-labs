def goroda(string: str):
    valid = ['минск', 'гродно', 'брест', 'могилев', 'витебск', 'гомель']
    return list(filter(lambda x: x.lower() in valid, string.split(' ')))


print(goroda(input()))
