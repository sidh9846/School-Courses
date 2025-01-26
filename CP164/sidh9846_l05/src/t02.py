"""
-------------------------------------------------------
Lab 5, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""

from functions import gcd

m = int(input("Enter M value: "))
n = int(input("Enter N value: "))

ans = gcd(m, n)

print(f"The GCD of {m} and {n} is {ans}")
