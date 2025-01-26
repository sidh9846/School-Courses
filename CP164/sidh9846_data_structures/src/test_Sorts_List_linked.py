"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-03-28"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here

    values = List()
    number = 0

    for i in range(SIZE):
        value = Number(number)
        values.append(value)
        number += 1

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here

    values = List()
    number = SIZE - 1

    for i in range(SIZE):
        value = Number(number)
        values.append(value)
        number -= 1

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here

    lists = []

    for i in range(TESTS):
        new_row = List()
        for i in range(SIZE):
            new_row.append(Number(random.randint(0, XRANGE)))

        lists.append(new_row)
        new_row = List()

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here

    # Create lists
    sorted = create_sorted()
    reversed = create_reversed()
    random = create_randoms()

    # init swap counter
    sorted_swaps = 0
    reversed_swaps = 0
    random_swaps = 0

    # init comp counter
    sorted_comp = 0
    reversed_comp = 0
    random_comp = 0

    # reset
    Sorts.swaps = 0
    Number.comparisons = 0

    # sorted
    func(sorted)
    sorted_swaps = Sorts.swaps
    sorted_comp = Number.comparisons

    # reset
    Sorts.swaps = 0
    Number.comparisons = 0

    # reversed
    func(reversed)
    reversed_swaps = Sorts.swaps
    reversed_comp = Number.comparisons

    # reset
    Sorts.swaps = 0
    Number.comparisons = 0

    # random
    # func(random)
    random_swaps = Sorts.swaps
    random_comp = Number.comparisons

    # reset
    Sorts.swaps = 0
    Number.comparisons = 0

    print(f"{title:<20s} {sorted_comp:<6} {reversed_comp:<8} {random_comp:<11} {sorted_swaps:<5} {reversed_swaps:<8} {random_swaps}")

    return
