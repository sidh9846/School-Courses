"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""

from functions import is_prime

num = int(input("Enter a number: "))

prime = is_prime(num)

if prime == False:
    print(f"{num} is not a prime number.")
elif prime == True:
    print(f"{num} is a prime number.")
