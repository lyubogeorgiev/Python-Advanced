rows, cols = [int(x) for x in input().split()]
START_VALUE = 97

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(row, cols + row):
        matrix[row].append(f'{chr(START_VALUE + row)}{chr(START_VALUE + col)}{chr(START_VALUE + row)}')

for m in matrix:
    print(' '.join(m))
