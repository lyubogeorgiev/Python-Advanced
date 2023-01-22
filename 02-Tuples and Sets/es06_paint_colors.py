import math
from collections import deque

colors = deque(input().split())
colors_list = []

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

while colors:

    first_mixer = colors.popleft()
    last_mixer = colors.pop() if colors else ""

    result_color_front = first_mixer + last_mixer
    result_color_back = last_mixer + first_mixer

    if result_color_front in main_colors or result_color_front in secondary_colors.keys():
        colors_list.append(result_color_front)
    elif result_color_back in main_colors or result_color_back in secondary_colors.keys():
        colors_list.append(result_color_back)
    else:
        if first_mixer:
            first_mixer = first_mixer[:len(first_mixer) - 1]
        if last_mixer:
            last_mixer = last_mixer[:len(last_mixer) - 1]

        middle_index = math.floor(len(colors) / 2)

        if last_mixer:
            colors.insert(middle_index, last_mixer)

        if first_mixer:
            colors.insert(middle_index, first_mixer)

valid_colors_list = []

for color in colors_list:

    # print(color)
    # print(set(secondary_colors[color]).issubset(main_colors))
    if color in main_colors:
        valid_colors_list.append(color)
    elif set(secondary_colors[color]).issubset(colors_list):
        valid_colors_list.append(color)
        # print(color)
        # print(secondary_colors[color])
        # print(set(secondary_colors[color]).issubset(colors_list))


print(valid_colors_list)

# print(colors_list)
# for color in colors_list:
#     if set(secondary_colors[color]).issubset(main_colors):
#         valid_colors_list.append(color)

# print(valid_colors_list)
# print([color for color in colors_list if secondary_colors[color] in main_colors or color in main_colors])
