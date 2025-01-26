"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-17"
-------------------------------------------------------
"""

from BST_linked import BST

bst = BST()

values = [5, 7, 3, 8, 6, 9, 4, 1]
values = [20, 10, 5, 4, 6, 15, 14, 16, 30, 25, 24, 26, 35, 34, 36]

[bst.insert(i) for i in values]


#[print(i) for i in bst]

# print(bst.retrieve(9))


print("inorder")
print(bst.inorder())
print("preorder")
print(bst.preorder())
print("postorder")
print(bst.postorder())
print("levelorder")
print(bst.levelorder())

bst.remove_root()
