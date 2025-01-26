"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""

from List_linked import List

values1 = [0, 1, 2, 3]

list = List()

[list.append(i) for i in values1]

p, c, i = list._linear_search_r(3)

print(p._value, c._value, i)
