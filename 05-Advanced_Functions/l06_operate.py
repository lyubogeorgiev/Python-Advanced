from functools import reduce


def operate(operator, *args):

    operation_dict = {
        '+': sum(args),
        '-': reduce(lambda a, b: a - b, args),
        '*': reduce(lambda a, b: a * b, args),
        '/': reduce(lambda a, b: a / b if b != 0 else 0, args)
    }

    return operation_dict[operator]


print(operate("+", 1, 2, 3))
