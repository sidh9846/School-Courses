"""
-------------------------------------------------------
Lab 2, Task 10
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-09-21"
-------------------------------------------------------
"""

food_charge = float(input("Food Charge: "))
sales_tax = float(input("Sales Tax in (%): "))
tip_percent = float(input("Tip in (%): "))

subtotal = food_charge
tax = food_charge * (sales_tax / 100)
tip = food_charge * (tip_percent / 100)
total = subtotal + tax + tip

print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Tip: $", tip)
print("------------------")
print("Total: $", total)
