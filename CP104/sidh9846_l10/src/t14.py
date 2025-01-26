"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""

from functions import file_copy_n

word_file = open("words.txt", "r")
copy_file = open("new_words.txt", "a")

print("Copying 'words.txt' to 'new_words.txt'")
num = int(input("Number of lines to copy: "))

file_copy_n(word_file, copy_file, num)

word_file.close()
copy_file.close()
