n = int(input())

elements = set()

for _ in range(n):
    [elements.add(element) for element in input().split()]

[print(element) for element in elements]
