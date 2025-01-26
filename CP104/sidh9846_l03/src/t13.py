"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-23"
-------------------------------------------------------
"""

seconds_input = int(input("Enter number of seconds: "))
seconds = seconds_input

hours = seconds // 3600
seconds = seconds - (hours * 3600)

minutes = seconds // 60
seconds = seconds - (minutes * 60)

print(
    f"There are {hours} hours, {minutes} minutes, and {seconds} seconds in {seconds_input} seconds")
