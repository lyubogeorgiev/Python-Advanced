text = input()

stack = []

for letter in text:
    stack.append(letter)

while stack:
    print(stack.pop(), end="")
