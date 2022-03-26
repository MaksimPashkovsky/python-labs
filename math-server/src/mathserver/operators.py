import math
import operator
from enum import Enum

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

# Enum for database
Operator = Enum('Operator', ' '.join([func.__name__.upper() for func in ALLOWED_OPERATIONS]))