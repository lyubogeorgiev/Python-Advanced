rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

# Traditional way to sum elements with loops
matrix_sum = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix_sum += matrix[row][col]

print(matrix_sum)


# Pythonic way to flatten and sum elements on a single line.
# print(sum([num for sublist in matrix for num in sublist]))
print(matrix)
