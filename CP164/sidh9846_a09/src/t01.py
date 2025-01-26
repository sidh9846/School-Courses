"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""

from functions import *
from Hash_Set_array import Hash_Set

fv = open("gibbon.txt", "r")

hash_set = Hash_Set(20)


insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)
