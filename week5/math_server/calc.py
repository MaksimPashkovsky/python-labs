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
    math.hypot
}


def do_calculation(data: str) -> str:
    try:
        operation, n1, n2 = data.split(' ')
        if hasattr(operator, operation) and getattr(operator, operation) in ALLOWED_OPERATIONS:
            result = getattr(operator, operation)(float(n1), float(n2))
        elif hasattr(math, operation) and getattr(math, operation) in ALLOWED_OPERATIONS:
            result = getattr(math, operation)(float(n1), float(n2))
        else:
            raise Exception
    except Exception:
        result = ''
    return str(result)
