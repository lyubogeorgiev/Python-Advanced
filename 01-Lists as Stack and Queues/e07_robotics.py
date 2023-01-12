robots = {}

input_robots = input().split(";")

for robot_time in input_robots:
    robot_tokens = robot_time.split("-")
    name = robot_tokens[0]
    time = int(robot_tokens[1])
    robots[name] = time

start_time_tokens = input().split(":")

hours = start_time_tokens[0]
minutes = start_time_tokens[1]
seconds = start_time_tokens[2]

while True:
    input_material = input()

    if input_material == "End":
        break


print(robots)

print("Start time: ")
print(f'Hours: {hours}')
print(f'Minutes: {minutes}')
print(f'Seconds: {seconds}')
