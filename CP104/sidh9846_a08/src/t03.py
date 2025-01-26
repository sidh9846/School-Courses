"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

from functions import common_ending

string1 = input("Type First String: ")

string2 = input("Type Second String: ")

common = common_ending(string1, string2)

print(f"The longest common ending of the two stings is \"{common}\".")
