input_text = input()

open_parenthesis = ['(', '{', '[']
close_parenthesis = [')', '}', ']']

isBalanced = True
stack = []

for symbol in input_text:
    if symbol in open_parenthesis:
        stack.append(symbol)
    else:
        if stack:
            current_open_parenthesis = stack.pop()
            open_index = open_parenthesis.index(current_open_parenthesis)
            close_index = close_parenthesis.index(symbol)
            if open_index != close_index:
                isBalanced = False
                break
        else:
            isBalanced = False
            break
if isBalanced:
    print("YES")
else:
    print("NO")
