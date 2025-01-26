"""
-------------------------------------------------------
Lab 10, Task 8
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""

from functions import append_increment

num_file = open("numbers.txt", "r+")

num = append_increment(num_file)

num_file.close()

print("file 'numbers.txt' open for reading and writing")
print(f"{num} is appended.")
