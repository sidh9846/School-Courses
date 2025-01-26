"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""

from Deque_linked import Deque

q1 = Deque()
q2 = Deque()
q3 = Deque()

values1 = [0, 1, 2, 3]
values2 = [99]
values3 = [99]

[q1.insert_rear(i) for i in values1]
[q2.insert_rear(i) for i in values2]
[q3.insert_rear(i) for i in values3]

print("Q1")
[print(i) for i in q1]
print("Q2")
[print(i) for i in q2]
print("Q3")
[print(i) for i in q3]

#print(q3 == q2)
print()
print("q1._swap(0, 1)")
q1._swap(0, 1)
print()
print("Q1")
[print(i) for i in q1]

print()
print("q1._rear._value")
print(q1._rear._value)
print("q1._front._value")
print(q1._front._value)
