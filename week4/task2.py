"""
Заказ
"""

from dataclasses import dataclass


@dataclass
class Dish:

    name: str
    price: float
    weight: int


class Order:

    def __init__(self, *args):
        self.__dishes = list()
        self.__dishes += list(args)
        self.__remain_sum = round(sum([dish.price for dish in self.__dishes]), 2)

    @property
    def dishes_quantity(self) -> int:
        return len(self.__dishes)

    @property
    def total_cost(self) -> float:
        return round(sum(d.price for d in self.__dishes), 2)

    @property
    def total_weight(self) -> int:
        return sum(d.weight for d in self.__dishes)

    def add_dish(self, d: Dish):
        self.__dishes.append(d)
        self.__remain_sum = round(self.__remain_sum + d.price, 2)

    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Wrong sum of payment!")
        a = round(self.__remain_sum - amount, 2)
        if a <= 0:
            print("Order has been paid, thank you")
            self.__remain_sum = 0
        else:
            self.__remain_sum = a

    def __repr__(self):
        return f"Order:\n" \
               f"Dishes: {self.__dishes},\n" \
               f"Dishes quantity: {self.dishes_quantity},\n" \
               f"Total cost: {self.total_cost},\n" \
               f"Total weight: {self.total_weight},\n" \
               f"Remaining sum: {self.__remain_sum}"


if __name__ == '__main__':
    d1 = Dish("Soup", 3.51, 250)
    d2 = Dish("Salad", 1.30, 160)
    d3 = Dish("Steak", 5.43, 310)

    order = Order(d1, d2)
    assert order.total_cost == 4.81
    assert order.dishes_quantity == 2
    assert order.total_weight == 410

    order.add_dish(d3)

    assert order.total_cost == 10.24
    assert order.dishes_quantity == 3
    assert order.total_weight == 720

    order.pay(10)
    print(order)
    order.pay(2)
    print(order)
    print("all tests passed")
