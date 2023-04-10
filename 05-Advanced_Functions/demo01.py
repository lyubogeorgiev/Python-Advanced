# name = "pesho"
# age = 32
# gender = "male"

def packing_example(**kwargs):
    return kwargs


print(packing_example(name='Pesho', age=32, gender='male'))


numbers = [1, 2, 3]


def sum_numbers(a, b, c):
    return sum((a, b, c))


print(sum_numbers(*numbers))


def print_args_kwargs(*args, **kwargs):
    print(f'Args: {args}, Kwargs: {kwargs}')


print(f'Invoking the function print_args_kwargs:')
print_args_kwargs('a', 'b', 'c', key1='value1', key2='value2')
