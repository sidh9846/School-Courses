"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""

from functions import interest_table

principal = float(input("Enter principal amount: "))
rate = float(input("Yearly interest rate: "))
payment = float(input("Monthly payment: "))

interest_table(principal, rate, payment)
