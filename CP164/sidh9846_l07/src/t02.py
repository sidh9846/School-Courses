"""
-------------------------------------------------------
Lab 7, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-06"
-------------------------------------------------------
"""

from List_linked import List

values1 = [0, 1, 2, 3, 4]

list1 = List()

[list1.append(i) for i in values1]

values2 = [0, 1, 1, 1]

list2 = List()

[list2.append(i) for i in values2]

even, odd = list1.split_alt_r()

[print(i) for i in even]
print("odd")
[print(i) for i in odd]
