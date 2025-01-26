"""
-------------------------------------------------------
Lab 11, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

from functions import generate_matrix_num

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
low = float(input("Enter low value: "))
high = float(input("Enter high value: "))
value_type = input("Enter value type ('float' or 'int'): ")


matrix = generate_matrix_num(rows, cols, low, high, value_type)

print(matrix)
