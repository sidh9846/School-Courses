"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import is_palindrome_stack

string = "racecar"
palindrome = is_palindrome_stack(string)
print(palindrome)
string = "Otto"
palindrome = is_palindrome_stack(string)
print(palindrome)
string = "Able was I ere I saw Elba"
palindrome = is_palindrome_stack(string)
print(palindrome)
string = "A man, a plan, a canal, Panama!"
palindrome = is_palindrome_stack(string)
print(palindrome)
string = "This is a Test!"
palindrome = is_palindrome_stack(string)
print(palindrome)
