"""
-------------------------------------------------------
Lab 6, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""

from List_linked import List

lst_linked = List()


list = [22, 33, 11, 55, 44]


for i in list:
    lst_linked.append(i)


for i in lst_linked:
    print(i)


print(lst_linked.index(22))
