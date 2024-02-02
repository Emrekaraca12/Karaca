def average_imdb_score(category : str) -> float:
    score_overall, count = 0, 0
    for movie in movies:
        if movie["category"] == category:
            score_overall += movie["imdb"]
            count += 1

    return score_overall / count

from movies import movies

print(average_imdb_score("Romance"))