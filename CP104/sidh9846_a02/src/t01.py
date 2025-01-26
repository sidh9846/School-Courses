"""
-------------------------------------------------------
Assignment 1, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

total = float(input("Enter the total sales: $"))

TAXRATE = 18.5

tax = total * TAXRATE / 100

print(f"""
Projected Tax Report
--------------------------
Total sales:   $ {total:,.2f}
Annual tax:    % {TAXRATE:.2f}
--------------------------
Tax:           $  {tax:,.2f}
""")
