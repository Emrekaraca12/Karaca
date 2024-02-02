def is_movie_imdb_above(category : str) -> list:
    from movies import movies
    same_categories = []

    for m in movies:
        if m["category"] == category:
            same_categories.append(m["name"])
    
    return same_categories


print(is_movie_imdb_above("War"))