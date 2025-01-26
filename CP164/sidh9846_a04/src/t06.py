"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""


from Priority_Queue_array import Priority_Queue

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

print("a" > "b")

key = "y"

print("key =", key)

target1, target2 = source.split_key(key)

print("target1")
[print(i) for i in target1]

print("target2")
[print(i) for i in target2]
