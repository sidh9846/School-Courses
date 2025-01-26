"""
-------------------------------------------------------
Testing for Task 5: sparse_matrix
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-18"
-------------------------------------------------------
"""
# Imports
from t05_functions import sparse_matrix

CASES = (
    "sparse1.txt",
    "sparse2.txt",
    "sparse3.txt"
)

for case in CASES:
    f_in = open(case, "r", encoding="utf-8")
    matrix = sparse_matrix(f_in)
    print(matrix)
    f_in.close()
    print()
