def is_movie_imdb_above() -> list:
    from movies import movies
    above_5_5 = []

    for m in movies:
        if m["imdb"] > 5.5:
            above_5_5.append(m["name"])
    
    return above_5_5


print(is_movie_imdb_above())