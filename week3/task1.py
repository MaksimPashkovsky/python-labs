import operator
import yaml


class ResultTooBigError(Exception):
    def __str__(self):
        return "The %s(%d, %d) is %d, but must be less than %d" % self.args


class ResultTooSmallError(Exception):
    def __str__(self):
        return "The %s(%d, %d) is %d, but must be bigger than %d" % self.args


OPERATIONS = {
    'sum': operator.add,
    'div': operator.truediv,
    'diff': operator.ne
}


def func(a: int, b: int, rules: dict):
    for operation, rule in rules.items():
        min_limit, max_limit = rule['min'], rule['max']
        result = OPERATIONS[operation](a, b)
        if min_limit <= result <= max_limit:
            continue
        try:
            raise ResultTooSmallError(operation, a, b, result, min_limit) if result < min_limit \
                else ResultTooBigError(operation, a, b, result, max_limit)
        except Exception as e:
            print(e.__class__.__name__, e)


if __name__ == '__main__':
    with open(r"week3\rules.yaml") as file:
        template = yaml.safe_load(file)
    func(100, 99, template)
