n = int(input())

matrix = [[int(el) for el in input().split(", ")] for row in range(n)]

# print(matrix)
even_matrix = [[el for el in row if el % 2 == 0] for row in matrix]

print(even_matrix)
# print([[el for el in row if el % 2 == 0]for row in matrix])
