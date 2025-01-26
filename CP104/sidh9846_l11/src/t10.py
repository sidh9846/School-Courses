"""
-------------------------------------------------------
Lab 11, Task 10
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

from functions import find_word_horizontal

matrix = [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]

word = input("Enter a word to search for: ")

rows = find_word_horizontal(matrix, word)

print(f"The word is located at index {rows}")
