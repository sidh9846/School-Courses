"""
-------------------------------------------------------
Lab 11, Task 7
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

from functions import find_position

matrix = [[-7, 5, 3], [3, 4, -2], [9, -8, -7], [0, -7, -6]]

s_loc, l_loc = find_position(matrix)

print(f"""The location of the smallest value is {s_loc}.
The location of the largest value is {l_loc}""")
