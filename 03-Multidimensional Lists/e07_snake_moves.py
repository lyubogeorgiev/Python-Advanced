rows, cols = [int(x) for x in input().split()]

word = input()

# print(word[1])

matrix = []
counter = 0

for m in range(0, rows):
    matrix.append([])

    for n in range(cols):
        current_index = counter % len(word)
        # print(f'Word lEnght: {len(word)}')
        # print(f'Counter: {counter}')
        # print(current_index)
        counter += 1
        if m % 2 == 0:
            matrix[m].append(word[current_index])
        else:
            matrix[m].insert(0, word[current_index])
        # for n in range(cols):
        #     current_index = counter % len(word)
        #     # print(f'Word lEnght: {len(word)}')
        #     # print(f'Counter: {counter}')
        #     # print(current_index)
        #     counter += 1
        #     matrix[m].insert(0, word[current_index])

for m in range(len(matrix)):
    print(''.join([x for x in matrix[m]]))
