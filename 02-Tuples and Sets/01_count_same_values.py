numbers = {}

number_list = map(float, input().split())

for number in number_list:
    if number not in numbers.keys():
        numbers[number] = 0

    numbers[number] += 1

[print(f'{round(key, 2)} - {value} times') for key, value in numbers.items()]
