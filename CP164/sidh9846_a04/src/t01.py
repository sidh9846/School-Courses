"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-13"
-------------------------------------------------------
"""

from Queue_circular import Queue

target = Queue()
source = Queue()
# target.insert(1)
# target.insert(2)
# target.insert(3)
# v = target.remove()
# print(v)
# v = target.peek()
# print(v)


# [print(i) for i in target]
[target.insert(i) for i in range(0, 8)]
[source.insert(i) for i in range(0, 9)]

# target.insert(3)

print(target == source)

# for i in target:
#     print(i)
