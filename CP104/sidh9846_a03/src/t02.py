"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

from functions import mow_lawn

width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))

time = mow_lawn(width, length, speed)

print(f"Mowing the lawn takes {time:.2f} minutes")
