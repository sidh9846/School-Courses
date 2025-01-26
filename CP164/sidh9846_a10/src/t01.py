"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""

from Sorts_array import Sorts

print("Unsorted:")
a = [456, 25, 7, -345, 1, 57, 4]

print(a)

Sorts.radix_sort(a)
print("Sorted:")
print(a)
