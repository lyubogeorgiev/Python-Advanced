n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

# print(matrix)

primary_diagonal = [matrix[n][n] for n in range(len(matrix))]
secondary_diagonal = [matrix[n][len(matrix) - 1 - n] for n in range(len(matrix))]

abs_value_diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(abs_value_diff)
