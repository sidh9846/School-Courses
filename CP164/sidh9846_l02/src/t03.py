"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-24"
-------------------------------------------------------
"""

from utilities import stack_to_array
from Stack_array import Stack


test = [1, 2, 3]
stack = Stack()
lst = []


for i in test:
    stack.push(i)

for i in stack:
    print(i)

stack_to_array(stack, lst)


print(lst)
