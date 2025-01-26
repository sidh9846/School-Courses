"""
-------------------------------------------------------
Assignment 6, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""

from functions import digit_count

num = abs(int(input("Enter a number: ")))

digits = digit_count(num)

print(f"{num} has {digits} digit(s).")
