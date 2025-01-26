"""
-------------------------------------------------------
Lab 7, Task 9
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-01"
-------------------------------------------------------
"""

from functions import get_int

high = int(input("Enter higest acceptable integer: "))
low = int(input("Enter lowest acceptable integer: "))

value = get_int(low, high)

print(value)
