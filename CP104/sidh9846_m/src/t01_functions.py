"""
-------------------------------------------------------
Midterm A Task 1 Function Definitions
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
# your code here


def total_coins(nickels, dimes, quarters, loonies):
    """
    -------------------------------------------------------
    Determines total amount of money in coins in cents.
        1 nickel = 5 cents
        1 dime = 10 cents
        1 quarter = 25 cents
        1 loonie = 100 cents
    Use: total = total_coins(nickels, dimes, quarters, loonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        total - total value of coins in cents (int)
    -------------------------------------------------------
    """

    # your code here

    total_nickels = nickels * NICKEL
    total_dime = dimes * DIME
    total_quarter = quarters * QUARTER
    total_loonie = loonies * LOONIE

    total = total_nickels + total_dime + total_quarter + total_loonie

    return total
