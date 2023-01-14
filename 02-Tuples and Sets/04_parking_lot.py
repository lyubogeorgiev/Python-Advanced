n = int(input())
garage = set()

for _ in range(n):
    command, car = input().split(", ")

    if command == "IN":
        garage.add(car)
    else:
        garage.remove(car)

if garage:
    print("\n".join(garage))
else:
    print("Parking Lot is Empty")
