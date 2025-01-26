"""
-------------------------------------------------------
Midterm A Task 4 Testing
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Imports
from t04_functions import categorize
# your testing code here
# must ask user to input test values
value = int(input("Enter a value: "))
category = categorize(value)
print(category)
