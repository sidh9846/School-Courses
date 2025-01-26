"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""

from functions import file_stats

fh = open("test.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()


print(f"There are {ucount} upper case letters, {lcount} lower case letters, {dcount} digits, and {wcount} whitespaces.")
