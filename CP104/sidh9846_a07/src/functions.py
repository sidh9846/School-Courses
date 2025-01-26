"""
-------------------------------------------------------
Assignment 7, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""


def list_factors(num):
    """
    -------------------------------------------------------
    Returns list of factors for a given number.
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - number to find factors for (int>0)
    Returns:
        factors - List of factors for num (list of int)
    ------------------------------------------------------
    """
    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    num = -1
    numbers = []

    while num != 0:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)
        else:
            pass

    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """

    locations = []

    for i in range(len(values)):
        if values[i] == target:
            locations.append(i)
        else:
            pass

    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in subtrahend:
        while i in minuend:
            minuend.remove(i)

    return minuend


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    in_order = False
    index = -1

    for i in range(len(values) - 1):
        if values[i] <= values[i + 1]:
            in_order = True
            index = -1
        else:
            in_order = False
            index = i + 1
            break

    return in_order, index
