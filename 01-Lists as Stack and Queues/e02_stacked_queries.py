def find_max_number(current_stack):
    current_max = current_stack[0]

    for num in current_stack:
        if num > current_max:
            current_max = num

    return current_max


def find_min_number(current_stack):
    current_min = current_stack[0]

    for num in current_stack:
        if num < current_min:
            current_min = num

    return current_min


n = int(input())

stack = []

for i in range(0, n):
    query_tokens = input().split(" ")

    query_code = int(query_tokens[0])

    if query_code == 1:
        stack.append(int(query_tokens[1]))

    elif query_code == 2:
        if stack:
            stack.pop()
    elif query_code == 3:
        print(find_max_number(stack))
    elif query_code == 4:
        print(find_min_number(stack))

while stack:
    print(stack.pop(), end="")

    if stack:
        print("", end=", ")
