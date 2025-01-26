"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""

from functions import student_info

students = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_info(students)
students.close()

print(f"""The student with the lowest grade was student {l_id}.
The student with the highest grade was student {h_id}.
The average was {avg:.2f}.""")
