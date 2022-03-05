class WrongArgumentError(Exception):

    def __init__(self, a_name, e_type, p_type):
        self.argument_name = a_name
        self.expected_type = e_type
        self.provided_type = p_type

    def __str__(self):
        return "'%s' argument must be %s, but %s provided" % self.args


def check_arguments(annotations: dict, params: dict):
    for name, class_instance in annotations.items():
        if not isinstance(params[name], class_instance):
            raise WrongArgumentError(name, class_instance, type(params[name]))


def func(a: str, b: int, c: dict, d: float):
    check_arguments(func.__annotations__, locals())
    print("All arguments are correct")


if __name__ == '__main__':
    func("111", 123, {1: 'asd'}, 1.0)
