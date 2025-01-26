"""
-------------------------------------------------------
Assignment 5, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-03"
-------------------------------------------------------
"""

from functions import range_total

start = int(input("Enter start value: "))
increment = int(input("Enter increment value: "))
count = int(input("Enter count value: "))

total = range_total(start, increment, count)

print(f"The total is {total}")
