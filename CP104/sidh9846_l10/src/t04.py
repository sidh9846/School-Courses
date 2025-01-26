"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""

from functions import customer_first

customer_file = open("customers.txt")
result = customer_first(customer_file)
customer_file.close()
print("Find customer with earliest sign-in:")
print(result)
