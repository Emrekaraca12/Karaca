def average_imdb_score(movies : list) -> float:
    score_overall = 0
    for movie in movies:
        score_overall += movie["imdb"]

    return score_overall / len(movies)

from movies import movies

print(average_imdb_score(movies))