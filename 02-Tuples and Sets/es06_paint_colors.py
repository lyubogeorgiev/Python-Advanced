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
    last_mixer = colors.pop()

    result_color = first_mixer + last_mixer

    if result_color in main_colors or result_color in secondary_colors.keys():
        colors_list.append(result_color)
    else:

