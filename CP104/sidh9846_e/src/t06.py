"""
-------------------------------------------------------
Testing for Task 6: rotate_list
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Imports
from copy import copy

from t06_functions import rotate_list

CASES = (
    ([], 5),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], -2),
    ([1, 2, 3, 4, 5], 13),
    ([1, 2, 3], 1),
    ([1, 2, 3], -1),
)

for case in CASES:
    # Make copy of testing value for printing purposes.
    values = copy(case[0])
    rotate_list(values, case[1])
    print(f"rotate_list({case[0]}, {case[1]}) → {values}")
    print()
