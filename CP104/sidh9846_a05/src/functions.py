"""
-------------------------------------------------------
Assignment 5, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-03"
-------------------------------------------------------
"""


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """

    product = 1

    for i in range(1, num):
        product = product * (i + 1)

    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes given 
    the number of calories burned per minute an the total number of minutes run
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - number of calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(5, minutes + 1, 5):
        cal_burned = i * per_minute

        print(f"{i:3}:{cal_burned:6.1f}")

    return


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints a triangle of '#' characters with an empty center.
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows (int)
    Returns:
        None
    ------------------------------------------------------
    """

    blank = " "

    for i in range(0, num_rows):
        space = blank * i
        print(f"#{space}#")

    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print("     ", end=" ")

    for i in range(start, stop + 1):
        print("    ", i, end=" ")

    print()
    print("     ", end=" ")

    for i in range(start, stop + 1):
        print("-------", end="")

    print("")

    for i in range(start, stop + 1):
        print(f"    {i} | ", end=" ")

        for j in range(start, stop + 1):
            product = i * j
            print(f"{product:3}   ", end=" ")

        print("")
    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    total = 0

    for i in range(start, (increment * count) + start, increment):
        total = total + i

    return total
