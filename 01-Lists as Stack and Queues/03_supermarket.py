from collections import deque

queue = deque()
while True:
    input_text = input()

    if input_text == "End":
        print(f'{len(queue)} people remaining.')
        break
    elif input_text == "Paid":
        while queue:
            print(queue.popleft())
        pass
    else:
        queue.append(input_text)
