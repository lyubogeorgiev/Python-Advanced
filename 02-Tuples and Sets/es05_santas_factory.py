from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

present_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}
is_crafted = False

while materials and magic_level:
    last_material = materials.pop()
    first_magic = magic_level.popleft()

    total_magic_level = last_material * first_magic

    if last_material == 0 and first_magic == 0:
        continue
    elif last_material == 0:
        magic_level.appendleft(first_magic)
        continue
    elif first_magic == 0:
        materials.append(last_material)
        continue

    if total_magic_level in present_table.keys():
        current_present = present_table[total_magic_level]
        if current_present not in crafted_presents.keys():
            crafted_presents[current_present] = 0

        crafted_presents[current_present] += 1
    elif total_magic_level < 0:
        materials.append(last_material + first_magic)
    elif total_magic_level > 0:
        last_material += 15
        materials.append(last_material)

first_set = {"Doll", "Wooden train"}
second_set = {"Teddy bear", "Bicycle"}

# print(first_set)
# print(second_set)
# print(set(present_table.values()))
# print(first_set.issubset(set(present_table.values())))

if first_set.issubset(set(crafted_presents.keys())) or second_set.issubset(set(crafted_presents.keys())):
    is_crafted = True
# is_crafted = True if first_set.issubset(set(present_table.values())) or second_set.issubset(set(present_table.values())) else False

presents_message = "The presents are crafted! Merry Christmas!" if is_crafted else "No presents this Christmas!"
print(presents_message)

materials.reverse()

print(f"Materials left: {', '.join(map(str, materials))}") if materials else ''
print(f"Magic left: {', '.join(map(str, magic_level))}") if magic_level else ''

[print(f"{key}: {value}") for key, value in crafted_presents.items()]
