"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here

    number = 0
    values = []

    while number < SIZE:
        values.append(Number(number))
        number += 1

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here

    number = SIZE - 1
    values = []

    while number >= 0:
        values.append(Number(number))
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
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here

    arrays = []

    for i in range(TESTS):
        new_row = []
        for i in range(SIZE):
            new_row.append(Number(random.randint(0, XRANGE)))

        arrays.append(new_row)
        new_row = []

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
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
    func(random)
    random_swaps = Sorts.swaps
    random_comp = Number.comparisons

    # reset
    Sorts.swaps = 0
    Number.comparisons = 0

    #print(f"{title:<20s} {sorted_comp:<6} {reversed_comp:<8} {random_comp:<11} {sorted_swaps:<5} {reversed_swaps:<8} {random_swaps}")
    print(f"{title}          {sorted_comp}     {reversed_comp}     {random_comp}        {sorted_swaps}     {reversed_swaps}     {random_swaps}")
    return
