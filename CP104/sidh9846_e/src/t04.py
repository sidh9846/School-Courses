"""
-------------------------------------------------------
Testing for Task 4: wide_triangle
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-18"
-------------------------------------------------------
"""
# Imports
from t04_functions import wide_triangle

CASES = list(range(1, 10))

for case in CASES:
    print(f'wide_triangle({case})')
    wide_triangle(case)
    print()
