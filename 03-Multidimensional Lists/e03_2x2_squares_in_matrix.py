def check_matrix(main_matrix, start_row, start_col):
    first_element = main_matrix[start_row][start_col]

    for m in range(start_row, start_row + 2):
        for n in range(start_col, start_col + 2):
            if first_element != matrix[m][n]:
                return 0

    return 1


rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

matrix_count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        matrix_count += check_matrix(matrix, row, col)

print(matrix_count)
