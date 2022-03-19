from typing import Union
from .operators import Operator, FUNC_OPERATOR_BY_NAME


def do_calculation(data: str) -> tuple[Operator, float, float, Union[float, str]]:
    en = Operator
    num1, num2 = 0, 0
    try:
        operation, n1, n2 = data.split(' ')

        num1 = float(n1)
        num2 = float(n2)

        op_func = FUNC_OPERATOR_BY_NAME[operation]

        result = op_func(float(n1), float(n2))

        en = Operator[operation.upper()]

    except (ValueError, KeyError, ZeroDivisionError, TypeError):
        result = ''

    return en, num1, num2, result
