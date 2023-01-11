from collections import deque

input_text = input()
n = int(input())

kids_list = input_text.split(" ")
kids_queue = deque()

for kid in kids_list:
    kids_queue.append(kid)

while len(kids_queue) > 1:
    for i in range(1, n):
        kids_queue.append(kids_queue.popleft())

    print(f'Removed {kids_queue.popleft()}')

print(f'Last is {kids_queue.popleft()}')
