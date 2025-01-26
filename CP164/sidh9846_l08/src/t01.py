"""
-------------------------------------------------------
Lab 8, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-03-14"
-------------------------------------------------------
"""

from morse import *
from BST_linked import BST

var = ByLetter("A", ".-")

bst = BST()

values = [("A", ".-"), ("A", ".-"), ("A", ".-")]


fill_letter_bst(bst, values)
fill_code_bst(bst, values)

code = "... --- ..."

#decode_morse(bst, code)

encode_morse(bst, code)
