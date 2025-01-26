"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""

from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()


temp = [54, 55764, 457, 542, 75, 3]

[a.insert_rear(i) for i in temp]

print("Unsorted:")
[print(i, end=", ") for i in a]

print()
Sorts.gnome_sort(a)

print("Sorted:")
[print(i, end=", ") for i in a]
