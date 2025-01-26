"""
-------------------------------------------------------
Assignment 6, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""

from functions import sum_factors

num = int(input("Enter a number: "))

total = sum_factors(num)

print(f"The sum of the factors of {num} is {total}.")
