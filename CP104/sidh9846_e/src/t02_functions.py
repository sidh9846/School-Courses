"""
-------------------------------------------------------
Exam Task 2 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Constants

# Your constants here
HOT_DAY = 28
PLEASANT_DAY_LOW = 16
PLEASANT_DAY_HIGH = 27
COLD_DAY = 15
SENTINEL_VALUE = -500


def temperatures():
    """
    -------------------------------------------------------
    Asks the user for daily high temperatures (in Celsius) from the keyboard.
    The function stops asking for temperatures when the user enters -500.
    The function returns:
        the total number of hot days (temperatures 28 or higher)
        the total number of pleasant days (temperatures 16 - 27)
        the total number of cold days (temperatures 15 or lower)
        the average temperature for all days (rounted down)
    Do all inputs and calculations in integer.
    Use: cold_days, pleasant_days, hot_days, avg_temp = temperatures()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        cold_days - number of cold days (int)
        pleasant_days - number of pleasant days (int)
        hot_days - number of hot days (int)
        avg_temp - average temperature of all days (int)
    -------------------------------------------------------
    """

    # Your code here

    user_input = int(input("Enter Temp:"))
    hot_days = 0
    pleasant_days = 0
    cold_days = 0
    total = 0
    count = 0

    while user_input != SENTINEL_VALUE:
        count += 1
        if user_input >= HOT_DAY:
            hot_days += 1
        elif PLEASANT_DAY_LOW <= user_input <= PLEASANT_DAY_HIGH:
            pleasant_days += 1
        elif user_input <= COLD_DAY:
            cold_days += 1
        total = total + user_input
        user_input = int(input("Enter Temperature: "))

    avg_temp = total // count

    return cold_days, pleasant_days, hot_days, avg_temp
