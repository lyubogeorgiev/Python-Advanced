n = int(input())

commands = input().split(', ')

matrix = []
squirrel_index = []

hazelnuts_collected = 0

is_squirrel_dead = False

command_map = {
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0),
    'up': (-1, 0)
}

for m in range(n):
    line = [x for x in input()]

    matrix.append(line)
    if 's' in line:
        squirrel_index.append(m)
        squirrel_index.append(line.index('s'))

        matrix[squirrel_index[0]][squirrel_index[1]] = '*'

for command in commands:
    squirrel_index[0] += command_map[command][0]
    squirrel_index[1] += command_map[command][1]

    if squirrel_index[0] >= n or squirrel_index[1] >= n:
        print('The squirrel is out of the field.')
        is_squirrel_dead = True
        break

    if matrix[squirrel_index[0]][squirrel_index[1]] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        is_squirrel_dead = True
        break

    if matrix[squirrel_index[0]][squirrel_index[1]] == 'h':
        hazelnuts_collected += 1
        matrix[squirrel_index[0]][squirrel_index[1]] = '*'
        if hazelnuts_collected == 3:
            break

if not is_squirrel_dead:
    if hazelnuts_collected == 3:
        print('Good job! You have collected all hazelnuts!')
    else:
        print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts_collected}')
