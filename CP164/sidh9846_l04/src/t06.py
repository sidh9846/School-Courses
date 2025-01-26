"""
-------------------------------------------------------
Lab 4, Task 6
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""

from List_array import List
from utilities import array_to_list
from utilities import list_to_array

lst = List()

list = []

for i in range(0, 10):
    lst.append(i)

# array_to_list(lst, source)
#
# print("source:", source)
#
# print("lst")
# for i in lst:
#     print(i, end=", ")

print("list before:", list)
print("lst before:")
for i in lst:
    print(i)

list_to_array(lst, list)

print("list after:", list)

print("lst after:")
for i in lst:
    print(i)
