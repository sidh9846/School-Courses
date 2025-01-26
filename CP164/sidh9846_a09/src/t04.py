"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""

from BST_linked import BST

bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(3)
bst.insert(7)
bst.insert(4)

zero_children, one_child, two_children = bst.node_counts()
print(zero_children)  # 2
print(one_child)  # 2
print(two_children)  # 1

print(bst.parent(4))
