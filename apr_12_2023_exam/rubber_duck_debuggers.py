from collections import deque

times = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

# first time multiply by last task

ducky_times = {
    'Darth Vader Ducky': [0, 60],
    'Thor Ducky': [61, 120],
    'Big Blue Rubber Ducky': [121, 180],
    'Small Yellow Rubber Ducky': [181, 240]
}

ducky_map = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times:
    current_time = times.popleft()
    current_value = tasks.pop()

    result_time = current_time * current_value

    for k, v in ducky_times.items():
        if v[0] <= result_time <= v[1]:
            ducky_map[k] += 1
            break

        if result_time > 240:
            current_value -= 2
            tasks.append(current_value)
            times.append(current_time)
            break

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print('\n'.join(f'{k}: {v}' for k, v in ducky_map.items()))
