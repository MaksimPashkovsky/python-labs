import multiprocessing
from typing import Union
from .operators import Operator, FUNC_OPERATOR_BY_NAME
import logging


def return_this(data: tuple, q):
    if q is not None:
        q.put(data)
    return data


def do_calculation(data: str, q: multiprocessing.Queue = None) -> \
        tuple[Operator, float, float, Union[float, str]]:
    """
    Receives the string, does the calculation
    If input data is correct result is float number, otherwise result is ''
    """
    logging.basicConfig(filename='calc.log', level=logging.INFO)
    op_enum = Operator
    num1, num2 = 0, 0

    splitted_data = data.split()

    if len(splitted_data) != 3:
        logging.error('Not enough/too many arguments!')
        return return_this((op_enum, num1, num2, ''), q)

    op_str, n1_str, n2_str = splitted_data

    if not op_str.isalpha() or op_str.lower() not in FUNC_OPERATOR_BY_NAME.keys():
        logging.error('Incorrect/not allowed operator!')
        return return_this((op_enum, num1, num2, ''), q)

    op_func = FUNC_OPERATOR_BY_NAME[op_str.lower()]
    op_enum = Operator[op_str.upper()]

    try:
        num1, num2 = float(n1_str), float(n2_str)
        result = op_func(num1, num2)
    except ValueError:
        logging.error('ValueError occurred!')
    except ZeroDivisionError:
        logging.error('ZeroDivisionError occurred!')
    except OverflowError:
        logging.error('Overflow occurred!')
        try:
            num1, num2 = int(n1_str), int(n2_str)
            result = op_func(num1, num2)
            return return_this((op_enum, num1, num2, result), q)
        except ValueError:
            return return_this((op_enum, num1, num2, 'Overflow'), q)
    else:
        return return_this((op_enum, num1, num2, result), q)

    return return_this((op_enum, num1, num2, ''), q)
