import math
from collections import deque
from functools import reduce

expression = deque(el for el in input().split())

nums = [1, 1, 1]

functions = {
    '+': lambda: reduce(lambda a, b: (a + b), nums),
    '-': lambda: reduce(lambda a, b: (a - b), nums),
    '*': lambda: reduce(lambda a, b: (a * b), nums),
    '/': lambda: reduce(lambda a, b: (a / b), nums),
}

while len(expression) > 1:
    nums.clear()

    while True:
        el = expression.popleft()
        if el not in functions.keys():
            nums.append(int(el))
            # print(nums)
        else:
            result = functions[el]()
            expression.appendleft(int(result))
            # print(result)
            break

print(expression[0])
