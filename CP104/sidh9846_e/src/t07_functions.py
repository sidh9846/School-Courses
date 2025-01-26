"""
-------------------------------------------------------
Exam Task 7 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""

DIGITS = "1234567890"


def file_split(f_in, f_digits, f_no_digits):
    """
    -------------------------------------------------------
    Copies the contents of f_in to f_digits and f_no_digits depending
    on the contents of f_in:
        Lines containing digits are copied to f_digits.
        Lines without digits are copied to f_no_digits.
        Empty lines are ignored.
    Use: file_split(f_in, f_digits, f_no_digits)
    -------------------------------------------------------
    Parameters:
        f_in - source file (file handle - already open for reading)
        f_digits - file to contain lines with digits from f_in (file handle
            - already open for writing)
        f_no_digits - file to contain non-empty lines without digits from f_n
            (file handle - already open for writing)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here

    line = f_in.readline()

    while line != '':
        length = len(line)
        count = 0
        for i in line:
            if i.isnumeric():
                f_digits.write(line)
                break
            count += 1
        if count == length:
            f_no_digits.write(line)
        line = f_in.readline()
