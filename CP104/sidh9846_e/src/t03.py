"""
-------------------------------------------------------
Testing for Task 3: alternate_case
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-18"
-------------------------------------------------------
"""
# Imports
from t03_functions import alternate_case

CASES = ('', 'ABC', 'abc', '123', 'This is the 3rd sentence.')

for case in CASES:
    print(f'alternate_case("{case}") → {alternate_case(case)}')
    print()
