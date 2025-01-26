"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

found_length = float(input("Foundation length (m): "))
found_width = float(input("Foundation width (m): "))
found_height = float(input("Foundation height (m): "))

wall_height = float(input("Wall height (m): "))

price_conc = float(input("Cost of concrete ($/m^3): "))
price_bricks = float(input("Cost of bricks ($/m^2): "))


conc_needed = found_length * found_width * found_height
cost_conc = conc_needed * price_conc

bricks_needed = ((found_length + found_width) * 2) * wall_height
cost_bricks = bricks_needed * price_bricks

total_cost = cost_conc + cost_bricks


print(f"""
Concrete needed for foundation (m^3): {conc_needed:,.2f}
Cost of concrete: ${cost_conc:,.2f}
Bricks needed for walls (m^2): {bricks_needed:,.2f}
Cost of bricks: ${cost_bricks:,.2f}
Total cost: ${total_cost:,.2f}
""")
