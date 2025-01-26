"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-29"
-------------------------------------------------------
"""

principal = float(input("Principal: $"))
interest = float(input("Interest (decimal): "))
years = int(input("Number of years: "))
timesPerYear = int(input("Number of times interest compounded per year: "))

balance = principal * (1 + (interest / timesPerYear)) ** (timesPerYear * years)

print(f"Balance: $ {balance}")
