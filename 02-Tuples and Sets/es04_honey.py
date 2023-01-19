from collections import deque

working_bees = deque(int(el) for el in input().split())
nectar = deque(int(el) for el in input().split())
honey_making_process = deque(el for el in input().split())

honey_made = 0

functions = {
    '+': lambda a, b: abs(a + b),
    '-': lambda a, b: abs(a - b),
    '*': lambda a, b: abs(a * b),
    '/': lambda a, b: abs(a / b)
}

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if first_bee <= last_nectar:
        first_symbol = honey_making_process.popleft()

        honey_made += functions[first_symbol](first_bee, last_nectar)
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {honey_made}")
print(f"Bees left: {', '.join(map(str, working_bees))}") if working_bees else ''
print(f"Nectar left: {', '.join(map(str, nectar))}") if nectar else ''
