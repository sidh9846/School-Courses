"""
-------------------------------------------------------
Lab 5, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""

from functions import recurse

x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))

ans = recurse(x, y)

print(f"The result of {x} and {y} is {ans}")
