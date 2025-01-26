"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""

from functions import population_growth

target = int(input("Enter target population: "))
current = int(input("Enter current population: "))
rate = float(input("Enter rate of growth: "))

years = population_growth(target, current, rate)

print(
    f"The number of years to reach a population of {target} will take {years} years")
