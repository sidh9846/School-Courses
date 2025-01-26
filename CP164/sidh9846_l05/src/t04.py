"""
-------------------------------------------------------
Lab 5, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""

from functions import to_power

base = float(input("Enter Base: "))
power = int(input("Enter Power: "))

ans = to_power(base, power)

print(f"{base} raised to {power} is {ans}")
