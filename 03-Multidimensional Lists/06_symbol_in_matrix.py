n = int(input())

matrix = [[el for el in input()] for row in range(n)]

search_symbol = input()

symbol_position = ()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if search_symbol == matrix[row][col]:
            symbol_position = (row, col)

            if symbol_position:
                break
    if symbol_position:
        break
print(f"{symbol_position}") if symbol_position else print(f"{search_symbol} does not occur in the matrix")
