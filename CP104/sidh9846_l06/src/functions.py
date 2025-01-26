"""
-------------------------------------------------------
Lab 6, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-27"
-------------------------------------------------------
"""


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    total = 0

    for i in range(start, finish + 1, increment):
        total = total + i

    return total


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, width):
        print(char * i)

    for i in range(width, 0, -1):
        print(char * i)

    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(start, end + inc, inc):
        cal_burned = i * burnt_per_minute
        print(f"Calories burned after {i} minutes: {cal_burned:.1f}")

    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    total_value = value

    print("Year       Value $")
    print("------------------")

    for i in range(years + 1):
        print(f"{i:<2d}      {total_value:10,.2f}")
        total_value = total_value * ((rate / 100) + 1)
        final_value = round(total_value / ((rate / 100) + 1), 2)

    return final_value


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    user_input = float(input("First value: "))
    minimum = user_input
    maximum = user_input
    total = user_input

    for i in range(n - 1):
        user_input = float(input("Next value: "))

        if user_input < minimum:
            minimum = user_input
        if user_input > maximum:
            maximum = user_input

        total = total + user_input

    average = total / n

    return minimum, maximum, total, average
