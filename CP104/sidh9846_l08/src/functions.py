"""
-------------------------------------------------------
Lab 8, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""
# imports
from random import randint


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """

    numbers = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

    name = numbers[n]

    return name


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """

    numbers = [randint(low, high)]

    while len(numbers) != n:
        new_number = randint(low, high)
        if new_number in numbers:
            pass
        else:
            numbers.append(new_number)

    return numbers


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """

    indexes = []

    for i in range(0, len(values)):
        if values[i] == value:
            indexes.append(i)
        else:
            pass

    return indexes


def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 ⋅ source2 [source1 dot product source2] (float)
    -------------------------------------------------------
    """

    target = 0

    for i in range(0, len(source1)):
        target = target + source1[i] * source2[i]

    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    target = []

    for i in range(0, len(source1)):
        if source1[i] not in source2 and source1[i] not in target:
            target.append(source1[i])

    for i in range(0, len(source2)):
        if source2[i] not in source1 and source2[i] not in target:
            target.append(source2[i])

    return target
