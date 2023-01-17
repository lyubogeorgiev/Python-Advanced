n = int(input())
usernames = set()

for _ in range(n):
    usernames.add(input())

[print(user) for user in usernames]
