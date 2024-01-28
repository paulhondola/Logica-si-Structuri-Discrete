movies = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
ratings = {1: 3, 2: 4, 3: 5, 4: 3, 5: 5}

from functools import reduce

def exists_in(movies, title):
    return title in movies.values()
 

# titlu -> 

def get_rating(movies, ratings, title):
    return reduce(lambda acc, pair: ratings[pair[0]] if pair[1] == title else acc ,movies.items(), -1)

print(get_rating(movies, ratings, 'A'))
