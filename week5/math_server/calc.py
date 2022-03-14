import operator


def do_calculation(data: str) -> str:
    try:
        operation, n1, n2 = data.split(' ')
        result = getattr(operator, operation)(float(n1), float(n2))
    except Exception:
        result = ''
    return str(result)
