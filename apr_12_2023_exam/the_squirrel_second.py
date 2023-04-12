n = int(input())

hazelnuts_collected = 0

commands = input().split(', ')
board = []

squirrel_coordinates = []

for row in range(n):
    current_row = [x for x in input()]
    if 's' in current_row:
        squirrel_coordinates.append(row)
        squirrel_coordinates.append(current_row.index('s'))
        current_row[squirrel_coordinates[1]] = '*'

    board.append(current_row)

moving_map = {
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0),
    'up': (-1, 0)
}

is_squirrel_dead = False

for command in commands:
    squirrel_coordinates[0] += moving_map[command][0]
    squirrel_coordinates[1] += moving_map[command][1]

    if squirrel_coordinates[0] >= n or squirrel_coordinates[1] >= n or squirrel_coordinates[0] < 0 \
            or squirrel_coordinates[1] < 0:
        print('The squirrel is out of the field.')
        is_squirrel_dead = True
        break
    elif board[squirrel_coordinates[0]][squirrel_coordinates[1]] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        is_squirrel_dead = True
        break
    elif board[squirrel_coordinates[0]][squirrel_coordinates[1]] == 'h':
        board[squirrel_coordinates[0]][squirrel_coordinates[1]] = '*'
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            break

if not is_squirrel_dead:
    if hazelnuts_collected == 3:
        print('Good job! You have collected all hazelnuts!')
    else:
        print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts_collected}')
