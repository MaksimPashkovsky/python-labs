import operator
import math

ALLOWED_OPERATIONS = {
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
    operator.floordiv,
    operator.pow,
    operator.mod,
    math.copysign,
    math.log,
    math.hypot
}

FUNC_OPERATOR_BY_NAME = {op.__name__: op for op in ALLOWED_OPERATIONS}


def do_calculation(data: str) -> str:
    try:
        operation, n1, n2 = data.split(' ')
        op_func = FUNC_OPERATOR_BY_NAME[operation]
        result = op_func(float(n1), float(n2))
    except (ValueError, KeyError, ZeroDivisionError, TypeError):
        result = ''
    return str(result)
