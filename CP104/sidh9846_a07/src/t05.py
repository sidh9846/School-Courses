"""
-------------------------------------------------------
Assignment 7, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""

from functions import is_sorted, list_positives

values = list_positives()
in_order, index = is_sorted(values)

if in_order:
    print("The list is sorted.")
else:
    print(f"The list is not sorted and breaks at index {index}.")
