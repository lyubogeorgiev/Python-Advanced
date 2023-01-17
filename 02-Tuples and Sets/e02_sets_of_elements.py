sets_length = list(map(int, input().split()))
# print(sets_length)


n = sets_length[0]

if len(sets_length) > 1:
    m = sets_length[1]
else:
    m = 0

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(input())

for _ in range(m):
    second_set.add(input())

# print(f'First Set: {first_set}')
# print(f'Second Set: {second_set}')

intersection_set = set(first_set).intersection(second_set)

[print(element) for element in intersection_set]
# print(intersection_set)
