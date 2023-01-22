import sys
# import numpy as np


def get_sum_of_matrix(current_matrix):
    matrix_sum = 0
    for row in current_matrix:
        for col in row:
            matrix_sum += int(col)

    return matrix_sum


rows, cols = [int(el) for el in input().split(", ")]

matrix = [[el for el in input().split(", ")] for row in range(rows)]

max_sum = -sys.maxsize - 1
max_square = []

for start_row in range(rows - 1):
    for start_col in range(cols - 1):

        current_matrix = [
            [matrix[start_row][start_col], matrix[start_row][start_col + 1]],
            [matrix[start_row + 1][start_col], matrix[start_row + 1][start_col + 1]]
        ]

        current_sum = get_sum_of_matrix(current_matrix)

        if current_sum > max_sum:
            max_square = current_matrix
            max_sum = current_sum

for row in range(2):
    print(f"{max_square[row][0]} {max_square[row][1]}")

# np_arr = np.array(max_square)
# print(np_arr)

# for row in max_square:
#     print([el for el in row], sep=" ")
# [print([el for el in row], sep=" ") for row in max_square]
print(max_sum)
