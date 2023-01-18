first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

functions = {
    '+': (lambda x)
}
for _ in range(int(input())):
    command, set_number, *data = input().split()

    if command == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")


