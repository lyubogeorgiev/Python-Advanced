odd_set = set()
even_set = set()

for row in range(int(input())):
    current_value = sum(ord(value) for value in (input())) // (row + 1)

    if current_value % 2 == 0:
        even_set.add(current_value)
    else:
        odd_set.add(current_value)

if sum(even_set) >= sum(odd_set):
    print(f"{', '.join(map(str, odd_set.union(even_set)))}")
else:
    print(f"{', '.join(map(str, odd_set.difference(even_set)))}")
