from collections import deque

needed_quantity = int(input())

input_tokens = input().split(" ")
orders_quantities = deque()
biggest_order = 0

for token in input_tokens:
    current_order_quantity = int(token)
    orders_quantities.append(current_order_quantity)
    if current_order_quantity > biggest_order:
        biggest_order = current_order_quantity

print(biggest_order)

while True:
    current_order = orders_quantities.popleft()

    if current_order <= needed_quantity:
        needed_quantity -= current_order
    else:
        orders_quantities.appendleft(current_order)
        break

    if not orders_quantities:
        break

if orders_quantities:
    print(f'Orders left: ', end="")
    while orders_quantities:
        print(orders_quantities.popleft(), end="")
        if orders_quantities:
            print("", end=" ")
else:
    print("Orders complete")
