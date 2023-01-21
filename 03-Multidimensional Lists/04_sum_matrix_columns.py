rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split()] for row in range(rows)]

# Traverse the Matrix
traversed_matrix = []
for col in range(cols):
    traversed_matrix.append([])

    for row in range(rows):
        traversed_matrix[col].append(matrix[row][col])

# print(traversed_matrix

for row in traversed_matrix:
    print(sum(row))
# column_sums = []

# for col in range(cols):
#     column_sums = sum([el for el in row for row in range(rows)])