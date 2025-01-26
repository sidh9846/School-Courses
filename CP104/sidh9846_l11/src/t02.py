"""
-------------------------------------------------------
Lab 11, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

from functions import generate_matrix_char

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = generate_matrix_char(rows, cols)

print(matrix)
