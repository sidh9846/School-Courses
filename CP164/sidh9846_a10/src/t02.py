"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""

from Sorts_List_linked import Sorts
from List_linked import List

a = List()

temp = [6, 356, 4, -789, 6, 2, 87]

[a.append(i) for i in temp]

print("Unsorted:")
[print(i, end=", ") for i in a]

print()
Sorts.radix_sort(a)

print("Sorted:")
[print(i, end=", ") for i in a]
