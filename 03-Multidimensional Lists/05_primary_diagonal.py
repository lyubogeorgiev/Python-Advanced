n = int(input())

matrix = [[int(el) for el in input().split()]for row in range(n)]

primary_diagonal_sum = 0

for i in range(n):
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)
