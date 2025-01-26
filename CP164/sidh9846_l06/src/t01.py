"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""

from List_linked import List

lst_linked = List()

v = 1

list = [22, 33, 11, 55, 44]


for i in list:
    lst_linked.append(i)

print("BEFORE")
for i in lst_linked:
    print(i)

lst_linked.insert(0, v)
print()

print("AFTER")
for i in lst_linked:
    print(i)
