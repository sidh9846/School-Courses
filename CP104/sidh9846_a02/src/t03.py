"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

date = int(input("Enter a date in the format DDMMYYYY: "))

day = date // 1000000
month = (date // 10000) % 100
year = date % 10000

print(f"The reformatted date: {year:02d}/{month:02d}/{day:02d}")
