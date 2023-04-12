n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

# print(matrix)

primary_diagonal = [matrix[n][n] for n in range(len(matrix))]

# for n in range(len(matrix)):
#     primary_diagonal.append(matrix[n][n])

# print(primary_diagonal)

secondary_diagonal = [matrix[n][len(matrix) - 1- n] for n in range(len(matrix))]

# for n in range(len(matrix)):
#     secondary_diagonal.append(matrix[n][len(matrix) - 1 - n])

# print(secondary_diagonal


def get_diagonal(diagonal_value, diagonal_type):
    # print(f'Diagonal type: {diagonal_type}')
    # print(f'Diagonal values: {", ".join([str(x) for x in diagonal_value])}')
    # print(f'Diagonal sum: {sum(diagonal_value)}')
    return f'{diagonal_type} diagonal: {", ".join([str(x) for x in diagonal_value])}. Sum: {sum(diagonal_value)}'


get_diagonal(primary_diagonal, "Primary")

print(get_diagonal(primary_diagonal, "Primary"))

print(get_diagonal(secondary_diagonal, "Secondary"))
