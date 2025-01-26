"""
-------------------------------------------------------
Lab 10, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-28"
-------------------------------------------------------
"""

from test_Sorts_array import *

# values = create_reversed()
#
# [print(i) for i in values]

# values = create_sorted()
#
# [print(i) for i in values]


title = "Bubble Sort"
test = title.lower().replace(" ", "_")
func = getattr(Sorts, test)

test_sort(title, func)


title = "Insertion Sort"

test = title.lower().replace(" ", "_")
func = getattr(Sorts, test)

test_sort(title, func)


title = "Shell Sort"

test = title.lower().replace(" ", "_")
func = getattr(Sorts, test)

test_sort(title, func)
