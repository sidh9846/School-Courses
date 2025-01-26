"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-12-01"
-------------------------------------------------------
"""

from functions import number_lines

fh_in = open("test.txt", "r", encoding="utf-8")
fh_out = open("test_numbered.txt", "w", encoding="utf-8")
number_lines(fh_in, fh_out)
fh_in.close
fh_out.close
