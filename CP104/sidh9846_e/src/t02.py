"""
-------------------------------------------------------
Testing for Task 2: temperatures
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-18"
-------------------------------------------------------
"""
# Imports
from t02_functions import temperatures

print("cold_days, pleasant_days, hot_days, avg_temp = temperatures()")
cold_days, pleasant_days, hot_days, avg_temp = temperatures()
print()
print(f"Cold days: {cold_days}")
print(f"Pleasant days: {pleasant_days}")
print(f"Hot days: {hot_days}")
print(f"Average temperature: {avg_temp} C")
