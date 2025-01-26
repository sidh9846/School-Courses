"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-14"
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set

# ht = Hash_Set(10)
#
# for i in range(20):
#     ht.insert(5)
#
# [print(i) for i in ht]

source = [55, 11, 22, 33, 44]
target = [55, 11, 22, 33, 44]

ht1 = Hash_Set(4)
ht2 = Hash_Set(4)

[ht1.insert(i) for i in source]
[ht2.insert(i) for i in target]


print(ht1.debug())

"""
5 Slots
----------------------------------------
Slot 0

55
----------------------------------------
Slot 1

11
----------------------------------------
Slot 2

22
----------------------------------------
Slot 3

33
----------------------------------------
Slot 4

44
"""
