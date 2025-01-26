"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""

from List_array import List

source1 = [44, 33, 55, 22, 55]
source2 = [22, 55, 11, 12]


lst1 = List()
[lst1.append(i) for i in range(5)]
#[lst1.append(i) for i in source1]
print("LST1")
[print(i) for i in lst1]

lst2 = List()
[lst2.append(i) for i in range(7)]
#[lst2.append(i) for i in source2]
print("LST2")
[print(i) for i in lst2]

lst3 = List()
#[lst3.append(i) for i in range(5)]
# lst3.append(55)
print("LST3")
[print(i) for i in lst3]

'''


# __eq__
print("__eq__")
print("lst1 == lst2:", lst1 == lst2)


# __getitem__
print("__getitem__")
print(lst1[1])


# append
print("append")
lst2.append(0)
print("LST2")
[print(i) for i in lst2]

# clean
print("clean")
lst2.clean()
print("LST2")
[print(i) for i in lst2]


# combine
print("combine")
lst3.combine(lst1, lst2)
print("LST3")
[print(i) for i in lst3]


# intersection
print("intersection")
lst3.intersection(lst1, lst2)
print("LST3")
[print(i) for i in lst3]


# prepend
print("prepend")
lst3.prepend(9)
print("LST3")
[print(i) for i in lst3]



# remove_front
print("remove_front")
value = lst2.remove_front()
print("value =", value)
print("LST2")
[print(i) for i in lst2]



# remove_many
print("remove_many")
lst2.remove_many(3)
print("LST2")
[print(i) for i in lst2]



# split
print("split")
target1, target2 = lst2.split()
print("target1")
[print(i) for i in target1]
print("target2")
[print(i) for i in target2]



# split_alt
print("split_alt")
target1, target2 = lst2.split_alt()
print("target1")
[print(i) for i in target1]
print("target2")
[print(i) for i in target2]


# union
print("union")
lst3.union(lst1, lst2)
print("LST3")
[print(i) for i in lst3]
'''
