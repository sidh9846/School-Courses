"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""

from Queue_array import Queue

source = Queue()
target = Queue()
print(source == target)
[source.insert(i) for i in range(1, 11)]
[target.insert(i) for i in range(1, 11)]

print(source == target)
