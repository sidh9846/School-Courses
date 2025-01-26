"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-13"
-------------------------------------------------------
"""

from functions import is_leap_year

for i in range(1800, 2100):
    if is_leap_year(i):
        print(i)
