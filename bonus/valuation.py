import csv
from collections import namedtuple

datas, currencies, matchings = [], {}, []

with open(r'D:\Python\pythonProject1\bonus\data.csv', newline="") as file:
    reader = csv.reader(file)
    Data = namedtuple('data', ",".join(next(reader)))
    while True:
        try:
            datas.append(Data(*next(reader)))
        except StopIteration:
            break
    # print(*datas, sep="\n")

with open(r'D:\Python\pythonProject1\bonus\currencies.csv', newline="") as file:
    reader = csv.reader(file)
    next(reader)  # first line
    while True:
        try:
            c = next(reader)
            currencies[c[0]] = c[1]
        except StopIteration:
            break
    print(currencies, sep="\n")


with open(r'D:\Python\pythonProject1\bonus\matchings.csv', newline="") as file:
    reader = csv.reader(file)
    Matching = namedtuple('matching', ",".join(next(reader)))
    while True:
        try:
            matchings.append(Matching(*next(reader)))
        except StopIteration:
            break
    # print(*matchings, sep="\n")

for i in range(1, len(matchings) + 1):
    ms = list(filter(lambda x: int(x.matching_id) == i, datas))
    total_price = sum([int(m.price) * int(m.quantity) for m in ms])




with open(r'D:\Python\pythonProject1\bonus\top_products.csv', 'w', newline='') as newfile:
    writer = csv.writer(newfile)
    writer.writerow(['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count'])