"""
-------------------------------------------------------
Lab 10, Task 12
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""

from functions import find_shortest

words_file = open("words.txt")
word = find_shortest(words_file)
words_file.close
print("file 'words.txt' open for reading")
print(f"'{word}' is the first shortest word")
