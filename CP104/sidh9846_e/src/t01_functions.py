"""
-------------------------------------------------------
Exam Task 1 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def max_diff(values):
    """
    -------------------------------------------------------
    Returns largest absolute difference between adjacent
    values in a list. Returns 0 if values has fewer than two elements.
    Use: md = max_diff(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        md - the largest absolute difference between adjacent numbers in values (int)
    -------------------------------------------------------
    """

    # Your code here
    print(values)
    length = len(values)
    md = 0

    if length < 2:
        md = None
    else:
        for i in range(length - 1):
            diff = abs(values[i] - values[i + 1])
            if diff > md:
                md = diff

    return md
