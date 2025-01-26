"""
-------------------------------------------------------
Exam Task 5 Function Definitions
Fall 2022
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""


def sparse_matrix(fh_in):
    """
    -------------------------------------------------------
    Creates a sparse matrix 2D list.
    Use: matrix = sparse_matrix(fh_in)
    -------------------------------------------------------
    Parameters:
        fh_in - the matrix file to process (file handle - already open for reading)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        matrix - a 2D list of the form:
            [ [row, col, value], [row, col, value], ... ] (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    matrix = []
    row = 0

    for i in fh_in:
        num = i.split(",")
        col = 0
        for j in num:
            if j.isnumeric() and j != "0":
                new_line = [row, col, int(j)]
                matrix.append(new_line)
            col += 1
        row += 1

    return matrix
