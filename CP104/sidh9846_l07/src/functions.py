"""
-------------------------------------------------------
Lab 7, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-01"
-------------------------------------------------------
"""

# imports
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """

    number = randint(1, high)
    guess = 0
    guesses = 0

    while guess != number:
        guess = int(input("Guess: "))
        guesses += 1

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Congratulations - good guess!")

    return guesses


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """

    pop = current
    years = 0

    while pop < target:
        years += 1
        pop = pop * ((rate / 100) + 1)

    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    number = float(input("First positive value: "))
    minimum = number
    maximum = number
    total = 0
    count = 0

    while number >= 0:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

        total = total + number

        count += 1
        number = float(input("Next positive value: "))

    average = total / count

    return minimum, maximum, total, average


# def num_categories():
#     """
#     -------------------------------------------------------
#     Asks a user to enter a series of numbers, then counts and returns
#     how may positives, negatives, and zeroes there are.
#     Stop processing values when the user enters -999.
#     Use: negatives, zeroes, positives = num_categories()
#     -------------------------------------------------------
#     Returns:
#         negatives - number of negative values (int)
#         zeroes - number of zero values (int)
#         positives - number of positive values (int)
#     ------------------------------------------------------
#     """
#
#     first_value = int(input("First value: "))
#
#     negatives = 0
#     zeros = 0
#     positives = 0
#
#     if first_value != -999:
#
#         next_value = int(input("Next value: "))
#
#         if first_value > 0:
#             positives += 1
#         elif first_value < 0:
#             negatives += 1
#         else:
#             zeros += 1
#
#         while next_value != -999 and first_value != -999:
#             if next_value > 0:
#                 positives += 1
#             elif next_value < 0:
#                 negatives += 1
#             else:
#                 zeros += 1
#
#             next_value = int(input("Next value: "))
#
#     return negatives, zeros, positives

def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """

    expenses = 0
    balance = available

    expense = float(input("Enter an expense (0 to quit): $"))

    while expense != 0:
        expenses = expenses + expense
        balance = balance - expense
        expense = float(input("Enter another expense (0 to quit): $"))

    if expenses < available:
        status = "Surplus"
    elif expenses > available:
        status = "Deficit"
    else:
        status = "Balanced"

    return expenses, balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """

    value = int(input(f"Enter a value between {low} and high {high}: "))

    while value > high or value < low:
        if value > high:
            print("Value entered is too high")
        elif value < low:
            print("Value entered is too low")

        value = int(input(f"Enter a value between {low} and high {high}: "))

    return value
