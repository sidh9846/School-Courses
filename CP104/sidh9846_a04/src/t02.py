"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-27"
-------------------------------------------------------
"""

from functions import pollution_level

aqi = int(input("Enter AQI: "))

level = pollution_level(aqi)

print(level)
