"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

from functions import date_extract

date_number = int(input("Enter a date in the format MMDDYYYY: "))

year, month, day = date_extract(date_number)

print(f"The reformatted date: {year}/{month}/{day}")
