from collections import deque

queue = deque()
dispenser_level = int(input())

while True:
    input_text = input()

    if input_text == "Start":
        break

    queue.append(input_text)

while True:
    input_text = input()

    if input_text == "End":
        break
    elif input_text.startswith("refill"):
        liters_to_add = int(input_text.split(" ")[1])
        dispenser_level += liters_to_add
    else:
        liters_needed = int(input_text)
        person_name = queue.popleft()
        if liters_needed <= dispenser_level:
            dispenser_level -= liters_needed
            print(f'{person_name} got water')
        else:
            print(f'{person_name} must wait')

print(f'{dispenser_level} liters left')
