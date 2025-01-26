"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

from functions import is_valid_isbn

isbn = input("Enter ISBN: ")

valid = is_valid_isbn(isbn)

if valid:
    print(f"The ISBN {isbn} is valid.")
else:
    print(f"The ISBN {isbn} is not valid.")
