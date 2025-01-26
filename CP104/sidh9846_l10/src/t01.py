"""
-------------------------------------------------------
Lab 10, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""

from functions import customer_record

customer_file = open("customers.txt")
print("Find record n")
record_num = int(input("Enter a record number: "))
result = customer_record(customer_file, record_num)
customer_file.close()

print(f"{result}")
