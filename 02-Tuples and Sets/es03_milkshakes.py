from collections import deque

chocolates = deque(int(el) for el in input().split(", "))
cups_of_milk = deque(int(el) for el in input().split(", "))

# print(chocolates)
# print(cups_of_milk)

milkshake_count = 0

while (chocolates and cups_of_milk) and milkshake_count < 5:
    last_chocolate = chocolates.pop()
    first_cup_of_milk = cups_of_milk.popleft()

    if last_chocolate <= 0 and first_cup_of_milk <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup_of_milk)
        continue
    elif first_cup_of_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_cup_of_milk:
        milkshake_count += 1
    else:
        cups_of_milk.append(first_cup_of_milk)
        last_chocolate -= 5
        chocolates.append(last_chocolate)

if milkshake_count >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, cups_of_milk)) if cups_of_milk else 'empty'}")
