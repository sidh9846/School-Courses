"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""

from Queue_array import Queue
from functions import queue_combine

Q1 = Queue()
Q2 = Queue()

source1 = []
source2 = [7, 9, 14]

[Q1.insert(i) for i in source1]
[Q2.insert(i) for i in source2]


result = queue_combine(Q1, Q2)

print("Result")

for i in result:
    print(i, end=" ")
