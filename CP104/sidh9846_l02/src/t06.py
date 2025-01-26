"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""


principal = int(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
year_rate = float(input("Yearly interest month_rate (%): "))
year_rate = year_rate / 100


months = years * 12
month_rate = year_rate / 12


top = month_rate * (1 + month_rate) ** months
bottom = ((1 + month_rate) ** months) - 1
payments = (top / bottom) * principal


print(payments)
