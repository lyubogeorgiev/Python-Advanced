names = set()

n = int(input())
# names = (input() for _ in range(n))

for _ in range(n):
    names.add(input())
print("\n".join(names))
# print(type(names))
