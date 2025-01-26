"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""

from functions import list_factors

num = int(input("Enter a number: "))

factors = list_factors(num)

print(f"The factors for {num} are {factors}.")
