n = int(input())

guest_list = [input() for _ in range(n)]
arrived_guests_list = []

# for _ in range(n):
#     guest_list.add(input())

while True:

    guest = input()

    if guest == "END":
        break

    arrived_guests_list.append(guest)

guests_has_not_arrived = set(guest_list).difference(arrived_guests_list)

print(len(guests_has_not_arrived))
# [print(guest) for guest in guests_has_not_arrived]

for guest_number in sorted(guests_has_not_arrived):
    print(guest_number)
