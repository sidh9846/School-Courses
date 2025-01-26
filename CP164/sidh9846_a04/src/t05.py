"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""

from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

source.insert("c")
source.insert("b")
source.insert("a")
source.insert("e")
source.insert("d")
source.insert("g")
source.insert("f")
source.insert("i")
source.insert("h")


# print(source.peek())

key = "e"

print("key =", key)

target1, target2 = pq_split_key(source, key)

print("target1")
[print(i) for i in target1]

print("target2")
[print(i) for i in target2]
