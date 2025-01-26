"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""

from functions import get_lotto_numbers

num = int(input("Number of values: "))
low = int(input("Low value of numbers: "))
high = int(input("High value of numbers: "))

numbers = get_lotto_numbers(num, low, high)

print(numbers)
