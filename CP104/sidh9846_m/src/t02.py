"""
-------------------------------------------------------
Midterm A Task 2 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Imports
from t02_functions import chess_rating

cases = (-1, 50, 1300, 2450, 2675, 3010)

for case in cases:
    rating = chess_rating(case)
    print(f"chess_rating({case}) → {rating}")
