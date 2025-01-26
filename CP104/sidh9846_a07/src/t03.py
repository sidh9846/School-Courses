"""
-------------------------------------------------------
Assignment 7, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""

from functions import list_indexes, list_positives

values = list_positives()
target = int(input("Enter a target: "))

indexes = list_indexes(values, target)

print(indexes)
