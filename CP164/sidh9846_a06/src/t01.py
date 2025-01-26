"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""

from Queue_linked import Queue

q1 = Queue()
q2 = Queue()
q3 = Queue()

values1 = [1, 2, 3, 4, 5]
values2 = [11, 22, 33, 44, 55]
values3 = []

[q1.insert(i) for i in values1]
[q2.insert(i) for i in values2]
[q3.insert(i) for i in values3]

print("Q1")
[print(i) for i in q1]
print()
print("Q2")
[print(i) for i in q2]
print()
print("Q3")
[print(i) for i in q3]


print()

print("q1.is_empty()")
print(q1.is_empty())
print("q1.is_empty()")
print(q3.is_empty())

print()


# q3._append_queue(q1)
# print()
#
# print("Q1")
# [print(i) for i in q1]
# print("Q2")
# [print(i) for i in q2]
# print("Q3")
# [print(i) for i in q3]
#
#
# target1, target2 = q2.split_alt()
#
# print("target1")
# [print(i) for i in target1]
# print("target2")
# [print(i) for i in target2]
# print("Q2")
# [print(i) for i in q2]
