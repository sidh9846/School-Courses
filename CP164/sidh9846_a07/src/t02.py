"""
-------------------------------------------------------
Assignment 7, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""

from Sorted_List_linked import Sorted_List

values1 = []
list1 = Sorted_List()
[list1.append(i) for i in values1]

values2 = []
list2 = Sorted_List()
[list2.append(i) for i in values2]

values3 = [11, 22, 33, 44, 55]
list3 = Sorted_List()
[list3.insert(i) for i in values3]


value = list3.remove(55)

print(value)

[print(i) for i in list3]
