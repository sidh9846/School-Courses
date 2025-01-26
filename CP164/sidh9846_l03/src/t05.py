"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-03"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq


pq = Priority_Queue()

test_lst = [55, 44, 11, 22, 33]


for i in test_lst:
    pq.insert(i)

print(array_to_pq(pq, test_lst))
