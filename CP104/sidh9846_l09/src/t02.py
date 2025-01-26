"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""

from functions import url_categorize

url = input("Enter URL: ")

url_type = url_categorize(url)

print(f"{url} is a {url_type} URL.")
