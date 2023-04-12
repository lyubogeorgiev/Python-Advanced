def invalid_coordinates(current_row, current_col, *coordinates):
    if coordinates[0] >= current_row or coordinates[1] >= current_col:
        return True

    if coordinates[2] >= current_row or coordinates[3] >= current_col:
        return True

    return False


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

# print(matrix)

while True:
    input_text = input()

    if input_text == "END":
        break

    command = input_text.split()

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    row_one = int(command[1])
    col_one = int(command[2])
    row_two = int(command[3])
    col_two = int(command[4])

    if invalid_coordinates(rows, cols, row_one, col_one, row_two, col_two):
        print('Invalid input!')
        continue

    temp = matrix[row_one][col_one]
    matrix[row_one][col_one] = matrix[row_two][col_two]
    matrix[row_two][col_two] = temp

    for m in matrix:
        print(' '.join(m))
