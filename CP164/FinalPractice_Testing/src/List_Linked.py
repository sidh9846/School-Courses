"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-12"
-------------------------------------------------------
"""

from List_linked import List

print("LIST1")
lst1 = List()
values1 = []
[lst1.append(i) for i in values1]
[print(i) for i in lst1]

print()

print("LIST2")
lst2 = List()
values2 = [2, 5, 6, 3]
[lst2.append(i) for i in values2]
[print(i) for i in lst2]

print()
print("LIST3")
lst3 = List()
values3 = [1, 2, 3]
[lst3.append(i) for i in values3]
[print(i) for i in lst3]

print()


lst3._move_front_to_rear(lst2)

print()

print("LIST1")
[print(i) for i in lst1]
# print(lst._front._next._next._next._next._next._value)

print("LIST2")

[print(i) for i in lst2]

print()

print("LIST3")

[print(i) for i in lst3]
