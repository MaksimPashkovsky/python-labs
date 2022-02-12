import re


def square_equation(equation: str):
    m = re.match(r"(-?\d+)x\^2 ([+-]\s?\d+)x ([+-]\s?\d+)", equation)
    a, b, c = map(lambda x: int(x.replace(" ", "")), m.groups())
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "Действительных корней нет"
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    return f"x1 = {x1}, x2 = {x2}"


print(square_equation("3x^2 - 7x + 2"))
