"""
-------------------------------------------------------
Assignment 8, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

from functions import is_word_chain

word_list = ['dog', 'god', 'dairy', 'yellow']

word_chain = is_word_chain(word_list)

if word_chain:
    print("The list is a word chain.")
else:
    print("The list is not a word chain.")
