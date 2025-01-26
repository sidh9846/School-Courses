"""
-------------------------------------------------------
Lab 2, Task 7
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))
volunteers = int(input("Number of volunteers: "))

fly_per_vol = flyers // volunteers
fly_leftover = flyers % volunteers

print(fly_per_vol)
print(fly_leftover)
