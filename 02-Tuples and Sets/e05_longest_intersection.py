longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = [first.split(",") for first in input().split("-")]

    first_set = set(range(int(first_range[0]), int(first_range[1]) + 1))
    second_set = set(range(int(second_range[0]), int(second_range[1]) + 1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is [{", ".join(map(str,longest_intersection))}] with length {len(longest_intersection)}')
