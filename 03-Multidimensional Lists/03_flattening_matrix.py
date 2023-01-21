n = int(input())

matrix = [[int(el) for el in input().split(", ")]for row in range(n)]

flattened_matrix = [el for sublist in matrix for el in sublist]

print(flattened_matrix)
