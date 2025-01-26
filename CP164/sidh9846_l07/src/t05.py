"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""

from List_linked import List

values1 = [22, 33, 11, 55, 44]
list1 = List()
[list1.append(i) for i in values1]

values2 = []
list2 = List()
[list2.append(i) for i in values2]

values3 = []
list3 = List()
[list3.append(i) for i in values3]


list3.union_r(list1, list2)

[print(i) for i in list3]
