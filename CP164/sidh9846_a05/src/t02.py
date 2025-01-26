"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""

from List_array import List
from Sorted_List_array import Sorted_List

source1 = [44, 33, 55, 22, 55]
source2 = [22, 55, 11, 12, 22]


lst1 = Sorted_List()
[lst1.insert(i) for i in range(6)]
#[lst1.insert(i) for i in source1]
print("LST1")
[print(i) for i in lst1]

lst2 = Sorted_List()
[lst2.insert(i) for i in range(0, 20, 2)]
#[lst2.insert(i) for i in source2]
print("LST2")
[print(i) for i in lst2]

lst3 = Sorted_List()
#[lst3.insert(5) for i in range(5)]
print("LST3")
[print(i) for i in lst3]

'''
# insert
print("insert")
lst1.insert(3)
lst1.insert(4)
print("LST1")
[print(i) for i in lst1]


# __contains__
print("__contains__")
print("test" in lst1)


# __eq__
print("__eq__")
print(lst3 == lst1)

# __getitem__
print("__getitem__")
print(lst1[3])



# clean
print("clean")
[lst1.insert(i) for i in range(5)]
print("LST1")
[print(i) for i in lst1]
lst1.clean()
print("LST1")
[print(i) for i in lst1]


# count
print("count")
print(lst3.count(5))



# find
print("find")
print(lst1.find(4))



# index
print("index")
print(lst2.index(15))



# intersection
print("intersection")
lst3.intersection(lst1, lst2)
print("LST3")
[print(i) for i in lst3]


# max
print("max")
print(lst2.max())


# min
print("min")
print(lst2.min())



# peek
print("peek")
print(lst1.peek())


# remove
print("remove")
print(lst2.remove(6))
print("LST2")
[print(i) for i in lst2]


# remove_front
print("remove_front")
print(lst1.remove_front())
print("LST1")
[print(i) for i in lst1]


# remove_many
print("remove_many")
lst3.remove_many(5)
print("LST3")
[print(i) for i in lst3]


# split
print("split")
target1, target2 = lst1.split()
print("target1")
[print(i) for i in target1]
print("target2")
[print(i) for i in target2]


# split_alt
print("split_alt")
target1, target2 = lst1.split_alt()
print("target1")
[print(i) for i in target1]
print("target2")
[print(i) for i in target2]



# split_key
print("split_key")
target1, target2 = lst2.split_key(22)
print("LST2")
[print(i) for i in lst2]
print("target1")
[print(i) for i in target1]
print("target2")
[print(i) for i in target2]



# union WORKS BUT WITH OUTSIDE METHOD (.insert())
print("union")
lst3.union(lst1, lst2)
print("LST3")
[print(i) for i in lst3]

'''
