from typing import Union
from .operators import Operator, FUNC_OPERATOR_BY_NAME


def do_calculation(data: str) -> tuple[Operator, float, float, Union[float, str]]:
    """
    Receives the string, does the calculation
    If input data is correct result is float number, otherwise result is ''
    """
    op_enum = Operator()
    num1, num2 = 0, 0

    splitted_data = data.split()

    if len(splitted_data) != 3:
        return op_enum, num1, num2, ''

    op_str, n1_str, n2_str = splitted_data

    if not op_str.isalpha() or op_str not in FUNC_OPERATOR_BY_NAME.keys():
        return op_enum, num1, num2, ''

    op_func = FUNC_OPERATOR_BY_NAME[op_str]
    op_enum = Operator[op_str.upper()]

    try:
        num1, num2 = float(n1_str), float(n2_str)
        result = op_func(num1, num2)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        return op_enum, num1, num2, result

    return op_enum, num1, num2, ''
