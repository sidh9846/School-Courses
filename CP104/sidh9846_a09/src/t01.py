"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""

from functions import file_head

fh = open("functions.py", "r", encoding="utf-8")

linecount = int(input("Enter number of lines: "))

file_head(fh, linecount)
fh.close()
