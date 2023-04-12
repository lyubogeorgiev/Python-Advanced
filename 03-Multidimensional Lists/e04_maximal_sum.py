def find_sum_of_3x3_matrix(main_matrix, start_row, start_col):
    sub_matrix_sum = 0

    for m in range(start_row, start_row + 3):
        sub_matrix_sum += sum([matrix[m][x] for x in range(start_col, start_col + 3)])

    return sub_matrix_sum


def get_sub_matrix_3x3(main_matrix, start_row, start_col):
    matrix_to_return = []

    for current_row in range(start_row, start_row + 3):
        matrix_to_return.append([main_matrix[current_row][x] for x in range(start_col, start_col + 3)])

    return matrix_to_return


rows, cols = [int(x) for x in input().split()]

begin_row_index = 0
begin_col_index = 0
max_sum = None

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for m in range(rows - 2):
    for n in range(cols - 2):
        current_sum = find_sum_of_3x3_matrix(matrix, m, n)
        if max_sum is None or max_sum < current_sum:
            max_sum = current_sum
            begin_row_index = m
            begin_col_index = n

result_matrix = get_sub_matrix_3x3(matrix, begin_row_index, begin_col_index)

print(f'Sum = {max_sum}')

for m in range(len(result_matrix)):
    print(' '.join(str(x) for x in result_matrix[m]))
