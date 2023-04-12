def sorting_cheeses(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda k: (-len(k[1]), k[0])))

    result_list = []

    for key, value in sorted_dict.items():
        result_list.append(key)
        result_list.extend(list(sorted(value, reverse=True)))

    return '\n'.join([str(x) for x in result_list])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
