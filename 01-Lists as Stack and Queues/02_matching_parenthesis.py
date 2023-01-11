input_text = input()

stack = []

for i in range(0, len(input_text)):
    if input_text[i] == '(':
        stack.append(i)
    elif input_text[i] == ')':
        start_index = stack.pop()
        print(input_text[start_index: i + 1])
