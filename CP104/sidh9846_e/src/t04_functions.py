"""
-------------------------------------------------------
Exam Task 4 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def wide_triangle(width):
    """
    -------------------------------------------------------
    Prints a triangle in which each succeeding line is 3 characters
    longer than the previous line.
    Use: wide_triangle(width)
    -------------------------------------------------------
    Parameters:
        width - maximum width in characters of triangle (int >= 1)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here

    # count = 0
    # length = 0
    #
    # while length <= width:
    #     length = (width % 3) + count
    #     print("#" * length)
    #     count += 3

    print("#" * width)
