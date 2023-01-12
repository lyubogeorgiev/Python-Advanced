input_tokens = input().split(" ")

rack_capacity = int(input())

racks = 1
current_rack_quantity = 0

while input_tokens:
    current_quantity = int(input_tokens.pop())

    if current_quantity + current_rack_quantity <= rack_capacity:
        current_rack_quantity += current_quantity
    else:
        racks += 1
        current_rack_quantity = current_quantity

print(racks)
