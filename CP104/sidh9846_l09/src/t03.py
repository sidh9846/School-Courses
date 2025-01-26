"""
-------------------------------------------------------
Lab 9, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""

from functions import parse_code

product_code = input("Enter code: ")

pc, pi, pq = parse_code(product_code)

print(f"""
Category: {pc}
ID: {pi}
Qualifier: {pq}
""")
