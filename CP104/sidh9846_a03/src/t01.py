"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

from functions import feet_to_acres

square_footage = float(input("Square footage: "))
acres = feet_to_acres(square_footage)

print(f"{acres:.2f} acres is equivalent to {square_footage:.2f} square feet")
