"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_split_alt

source = Stack()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lst:
    source.push(i)


target1, target2 = stack_split_alt(source)


print("target1")
for i in target1:
    print(i)

print("target2")
for i in target2:
    print(i)
