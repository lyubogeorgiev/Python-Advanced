from collections import deque

expression = deque(el for el in input().split())

print(expression)
print(expression.popleft())
print([el for el in expression])
