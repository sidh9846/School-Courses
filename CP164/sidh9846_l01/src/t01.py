"""
-------------------------------------------------------
Lab 1, Testing File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-13"
-------------------------------------------------------
"""

from Movie import Movie
from Movie_utilities import *

movie1 = Movie("Movie1", 2020, "John", 7.6, [0, 2])

#print(read_movie("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8"))


fh = open("movies.txt", "r")
line = fh.readline()

while line != "":
    print(read_movie(line))
    line = fh.readline()
    print()
