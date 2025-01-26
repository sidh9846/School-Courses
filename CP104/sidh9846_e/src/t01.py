"""
-------------------------------------------------------
Testing for Task 1: max_diff
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Imports
from t01_functions import max_diff

CASES = (
    [],
    [99],
    [1, 2, 3],
    [-5, 5, 0, 9],
)

for case in CASES:
    print(f'max_diff({case}) → {max_diff(case)}')
    print()
