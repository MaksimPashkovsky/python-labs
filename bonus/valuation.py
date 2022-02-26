import csv
from collections import namedtuple


def read_file(filename, name: str):
    with open(r'bonus\\' + filename, newline="") as file:
        reader = csv.reader(file)
        this_tuple = namedtuple(name, ",".join(next(reader)))
        return [this_tuple(*n) for n in reader]


if __name__ == '__main__':
    datas = read_file('data.csv', 'data')
    currencies = read_file('currencies.csv', 'currency')
    matchings = read_file('matchings.csv', 'matching')

    with open(r'bonus\top_products.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count'])

        # matching_id's iteration
        for cur_id in range(1, len(matchings) + 1):
            # only products with current matching_id
            products = list(filter(lambda x: int(x.matching_id) == cur_id, datas))

            # sort products according to total price and currency
            sorted_products = sorted(products, key=
                    lambda x: int(x.price)
                              * int(x.quantity)
                              * float(
                                    next(
                                        filter(lambda y: y.currency == x.currency, currencies)).ratio)
                                    )

            # products limit for current matching_id
            limit = int(
                next(
                    filter(lambda x: int(x.matching_id) == cur_id, matchings)
                ).top_priced_count
            )

            ignored = abs(limit - len(products))
            while limit:
                prod = sorted_products.pop()
                total_price = int(prod.price) * int(prod.quantity)
                avg_price = total_price / int(prod.quantity)
                currency = prod.currency
                writer.writerow([cur_id, total_price, round(avg_price), currency, ignored])
                limit -= 1
