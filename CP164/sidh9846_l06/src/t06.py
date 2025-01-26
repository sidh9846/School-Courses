"""
-------------------------------------------------------
Lab 6, Task 6
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""

from List_linked import List

lst_linked1 = List()
lst_linked2 = List()


list1 = [11, 22, 33, 44]
list2 = [44, 33, 22, 11]


for i in list1:
    lst_linked1.append(i)

for i in list2:
    lst_linked2.append(i)


for i in lst_linked1:
    print(i)

for i in lst_linked2:
    print(i)


print("eq", lst_linked1 == lst_linked2)
