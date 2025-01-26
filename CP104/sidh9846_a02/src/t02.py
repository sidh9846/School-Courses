"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

number = int(input("Enter a positive digit number: "))

first = number // 10
second = number % 10

product = first * second

print(f"The product of the digits of {number} is {product}")
