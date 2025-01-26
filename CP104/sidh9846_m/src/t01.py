"""
-------------------------------------------------------
Midterm A Task 1 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-10-29"
-------------------------------------------------------
"""
# Imports
from t01_functions import total_coins

CASES = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 1, 1, 1),
    (10, 10, 10, 10)
)
for case in CASES:
    nickels = case[0]
    dimes = case[1]
    quarters = case[2]
    loonies = case[3]
    total = total_coins(nickels, dimes, quarters, loonies)
    print(f"total_coins{case} → {total}")
