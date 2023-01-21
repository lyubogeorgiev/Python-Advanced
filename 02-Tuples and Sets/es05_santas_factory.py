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

    # print(f"Materials: {materials}")
    # print(f"Magic Level: {magic_level}")
    # print(f"First Material: {materials[0]}")
    # print(f"Last Magic: {magic_level[len(magic_level) - 1]}")
    # print("----------")

    # if materials[len(materials) - 1] == 0 or magic_level[0] == 0:
    #     if materials[len(materials) - 1] == 0 and magic_level[0] != 0:
    #         materials.pop()
    #         continue
    #     elif materials[0] != 0 and magic_level[len(magic_level) - 1] == 0:
    #         magic_level.popleft()
    #         continue
    #     else:
    #         materials.pop()
    #         magic_level.popleft()
    #         continue

    last_material = materials.pop()
    first_magic = magic_level.popleft()

    total_magic_level = last_material * first_magic

    if total_magic_level in present_table.keys():
        current_present = present_table[total_magic_level]
        if current_present not in crafted_presents.keys():
            crafted_presents[current_present] = 0

        crafted_presents[current_present] += 1
    else:
        if total_magic_level < 0:
            sum_values = last_material + first_magic
            materials.append(sum_values)

        if total_magic_level > 0:
            last_material += 15
            materials.append(last_material)

        if total_magic_level == 0:
            if last_material != 0:
                materials.append(last_material)

            if first_magic != 0:
                magic_level.appendleft(first_magic)

first_set = {"Doll", "Wooden train"}
second_set = {"Teddy bear", "Bicycle"}

if first_set.issubset(set(crafted_presents.keys())) or second_set.issubset(set(crafted_presents.keys())):
    is_crafted = True

presents_message = "The presents are crafted! Merry Christmas!" if is_crafted else "No presents this Christmas!"
print(presents_message)

print(f"Materials left: {', '.join([str(material) for material in materials][::-1])}") if materials else ''
print(f"Magic left: {', '.join(str(el) for el in magic_level)}") if magic_level else ''

[print(f"{key}: {value}") for key, value in sorted(crafted_presents.items())]
