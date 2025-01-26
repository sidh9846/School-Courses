"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""

from Priority_Queue_linked import Priority_Queue

q1 = Priority_Queue()
q2 = Priority_Queue()
q3 = Priority_Queue()

values1 = [1, 2, 3, 4, 5, 3]
values2 = [4]
values3 = []

[q1.insert(i) for i in values1]
[q2.insert(i) for i in values2]
[q3.insert(i) for i in values3]

print("Q1")
[print(i) for i in q1]
print("Q2")
[print(i) for i in q2]
print("Q3")
[print(i) for i in q3]


q3.combine(q1, q2)

# q2._append_queue(q1)
# print()
#
# print("Q1")
# [print(i) for i in q1]
# print("Q2")
# [print(i) for i in q2]
# print("Q3")
# [print(i) for i in q3]
#
# print(q2._rear._value)
