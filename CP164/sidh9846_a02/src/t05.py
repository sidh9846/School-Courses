"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""

from Movie import Movie
from Movie_utilities import genre_counts, read_movie

file = open("movies.txt", "r")
line = file.readline()
movies = []

while line != "":
    movie = read_movie(line)
    movies.append(movie)
    line = file.readline()


# m1 = Movie("Movie1", 2021, "Director1", 3.4, [1, 3, 6])
# m2 = Movie("Movie2", 2021, "Director2", 6.4, [0, 7, 9])
# print(m1, m2)
#
# print(genre_counts([m1, m2]))

counts = genre_counts(movies)

print(f"Counts for movie.txt = {counts}")
