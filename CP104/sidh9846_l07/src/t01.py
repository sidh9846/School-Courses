"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-01"
-------------------------------------------------------
"""

from functions import hi_lo_game

max = int(input("Maximum value?: "))

count = hi_lo_game(max)

print(f"You made {count} guesses.")
