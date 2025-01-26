"""
-------------------------------------------------------
Assignment 3 Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""

# CONSTANTS
SQUARE_FT_PER_ACRE = 43560

# IMPORTS
from random import randint


def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """

    acres = square_footage / SQUARE_FT_PER_ACRE
    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """

    area = length * width
    time = area / speed

    return time


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """

    month = date_number // 1000000
    day = (date_number // 10000) % 100
    year = date_number % 10000

    return year, month, day


def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """

    numerator = num1 * num2
    denominator = denom1 * denom2

    product = numerator / denominator

    return numerator, denominator, product


def math_quiz():
    """
    -------------------------------------------------------
    Displays two random numbers between 0 and 999 that are to be added, asks a user to enter an answer, 
    then displays the user answer along with the expected answer.
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    ------------------------------------------------------
    """

    number1 = randint(0, 999)
    number2 = randint(0, 999)
    answer = number1 + number2

    print(f"{number1:5d}")
    print(f"+{number2:4d}")

    print()

    user_answer = int(input("Your answer: "))

    print()

    print(f"Your answer:{user_answer:4d}")
    print(f"Expected:{answer:7d}")

    return
