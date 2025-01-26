"""
-------------------------------------------------------
Midterm A Task 4 Function Definitions
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""


def categorize(value):
    """
    DO NOT CHANGE THE CONTENTS OF THIS FUNCTION
    -------------------------------------------------------
    Determines whether a value is positive, negative, or zero.
    Use: category = categorize(value)
    -------------------------------------------------------
    Parameters:
        categorize - an integer to categorize (int)
    Returns:
        category - whether value is positive, negative, or zero (str)
    -------------------------------------------------------
    """
    if value > 0:
        category = 'positive'
    elif value < 0:
        category = 'negative'
    else:
        category = 'zero'
    return category
