"""
-------------------------------------------------------
Lab 5, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""

from functions import is_palindrome

s = input("Enter string: ")
# s = "racec!ar"

palindrome = is_palindrome(s)


print(f"'{s}' is a palindrome") if palindrome else print(
    f"'{s}' is a palindrome")
