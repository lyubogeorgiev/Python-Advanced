first = set(int(num) for num in input().split())
second = set(int(num) for num in input().split())

functions = {
    'Add First': (lambda x: [first.add(int(el)) for el in x]),
    'Add Second': (lambda x: [second.add(int(el)) for el in x]),
    'Remove First': (lambda x: [first.discard(int(el)) for el in x]),
    'Remove Second': (lambda x: [second.discard(int(el)) for el in x]),
    'Check Subset': lambda x: print("True")
    if first.issubset(second) or second.issubset(first) else print("False")
}

for _ in range(int(input())):
    command, set_number, *data = input().split()

    functions[command + " " + set_number](data if data else '')

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
