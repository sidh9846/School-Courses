"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""

FREEZING = 32
temp_cel = int(input("Temperature (C): "))
temp_fer = int(temp_cel * (9 / 5) + FREEZING)


if temp_cel >= -173:
    print(temp_fer)
else:
    print("Invaild Input!")
