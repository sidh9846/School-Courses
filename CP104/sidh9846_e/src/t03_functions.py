"""
-------------------------------------------------------
Exam Task 3 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def alternate_case(string):
    """
    -------------------------------------------------------
    Converts letters in a string to alternate case. Letters
    at an even index are converted to (or left as) upper-case,
    Letters at an odd index are converted to (or left as)
    lower-case. Non-letters are ignored.
    Use: alternating = alternate_case(string)
    -------------------------------------------------------
    Parameters:
        width - maximum width in characters of triangle (int >= 1)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        alternating - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here
    length = len(string)
    alternating = ''

    for i in range(length):
        if i % 2 == 0 and string[i].isalpha():
            alternating += string[i].upper()
        elif string[i].isalpha():
            alternating += string[i].lower()
        else:
            alternating += string[i]

    return alternating
