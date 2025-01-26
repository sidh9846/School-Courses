"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""

from List_linked import List

values1 = [11, 22, 33, 44, 55]
list1 = List()
[list1.append(i) for i in values1]

values2 = [5, 6, 7, 8]
list2 = List()
[list2.append(i) for i in values2]

values3 = [11, 22, 33, 44]
list3 = List()
[list3.append(i) for i in values3]


target1, target2 = list3.split()

[print(i) for i in target1]
print(2)
[print(i) for i in target2]
