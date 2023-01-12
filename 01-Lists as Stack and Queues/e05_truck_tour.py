from collections import deque

n = int(input())
tank_level = 0
pumps_queue = deque()
pump_number = 0
starting_pump = 0

for _ in range(0, n):
    input_tokens = input().split()
    int_tokens = [int(input_tokens[0]), int(input_tokens[1])]

    pumps_queue.append(int_tokens)

while pumps_queue:
    pump_number += 1
    current_pump = pumps_queue.popleft()
    fuel_to_put = current_pump[0]
    distance_to_travel = current_pump[1]

    new_tank_level = fuel_to_put + tank_level
    if new_tank_level >= distance_to_travel:
        tank_level = new_tank_level - distance_to_travel
    else:
        pumps_queue.append(current_pump)
        starting_pump = pump_number

print(starting_pump)
