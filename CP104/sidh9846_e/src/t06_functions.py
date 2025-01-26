"""
-------------------------------------------------------
Exam Task 6 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def rotate_list(values, n):
    """
    -------------------------------------------------------
    Rotates the elements in values n places:
        A positive n rotates elements from the front to the rear of values.
        A negative n rotates elements from the rear to the front of values.
    Use: rotate_list(values, n)
    -------------------------------------------------------
    Parameters:
        values - list of elements to rotate (list of *)
        n - number of places to rotate values (int)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here

    index = n
    # length = len(values)
    #
    # while index > length:
    #     index = index - length

    values = values[index:] + values[:index]
