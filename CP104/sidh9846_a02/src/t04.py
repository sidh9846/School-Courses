"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

pieces = int(input("Number of pieces of cake: "))
people = int(input("Number of party-goers: "))

recived = pieces // people
leftover = pieces % people

print(f"""
Each party-goer receives {recived} pieces of cake
Pieces of cake that won’t be distributed: {leftover}
""")
