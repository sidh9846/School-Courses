"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-24"
-------------------------------------------------------
"""

from utilities import array_to_stack
from Stack_array import Stack

stack = Stack()

print(array_to_stack(stack, [1, 2, 3]))

for i in stack:
    print(i)
