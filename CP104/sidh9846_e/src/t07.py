"""
-------------------------------------------------------
Testing for Task 7: file_split
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Imports
from t07_functions import file_split


# Your code here
f_in = open("source.txt", "r")
f_digits = open("digits.txt", "w")
f_no_digits = open("no_digits.txt", "w")

file_split(f_in, f_digits, f_no_digits)

f_in.close()
f_digits.close()
f_no_digits.close()
