"""
-------------------------------------------------------
Lab 7, Task 8
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-01"
-------------------------------------------------------
"""

from functions import budget

available = float(input("Money available: $"))

expenses, balance, status = budget(available)

print(f"""
Expenses were ${expenses:.2f}.
The balance is ${balance:.2f}.
The budget is (in) {status}.
""")
