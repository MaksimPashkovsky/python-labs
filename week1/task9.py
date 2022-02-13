def fio_parse(string: str):
    return " ".join([st.capitalize() for st in string.split(' ', 3)[:3]])


print(fio_parse(input()))
