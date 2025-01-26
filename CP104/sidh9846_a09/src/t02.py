"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

from functions import file_integers

fh = open("numbers.txt", "r", encoding="utf-8")
numbers = file_integers(fh)
fh.close()

print(numbers)
