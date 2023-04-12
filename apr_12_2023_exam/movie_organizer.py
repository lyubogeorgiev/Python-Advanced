def movie_organizer(*args):
    movie_storage = {}

    for movie in args:
        movie_name = movie[0]
        genre = movie[1]

        if genre not in movie_storage.keys():
            movie_storage[genre] = []

        movie_storage[genre].append(movie_name)

    for key in movie_storage.keys():
        movie_storage[key] = sorted(movie_storage[key])

    movie_storage_list = sorted(movie_storage, key=lambda k: (-len(movie_storage[k]), k))

    result_list = []

    for name in movie_storage_list:
        result_list.append(f'{name} - {len(movie_storage[name])}')
        result_list.extend([f'* {x}' for x in movie_storage[name]])

    return '\n'.join(result_list)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
