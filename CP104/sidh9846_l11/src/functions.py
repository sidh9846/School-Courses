"""
-------------------------------------------------------
Lab 11, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""

import random

ALPHA = "abcdefghijklmnopqrstuvwxyz"


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    matrix = []

    for i in range(rows):
        new_row = []
        if value_type == "int":
            for j in range(cols):
                new_row.append(random.randint(low, high))
        elif value_type == "float":
            for j in range(cols):
                new_row.append(random.uniform(low, high))
        matrix.append(new_row)

    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """

    matrix = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(ALPHA[random.randint(0, 25)])
        matrix.append(new_row)

    return matrix


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """

    s_row = -1
    s_col = -1
    smallest = matrix[0][0]
    s_loc = [0, 0]

    l_row = -1
    l_col = -1
    largest = matrix[0][0]
    l_loc = [0, 0]

    for i in matrix:
        s_row += 1
        s_col = -1
        for j in i:
            s_col += 1
            if j < smallest:
                smallest = j
                s_loc[0] = s_row
                s_loc[1] = s_col

    for i in matrix:
        l_row += 1
        l_col = -1
        for j in i:
            l_col += 1
            if j > largest:
                largest = j
                l_loc[0] = l_row
                l_loc[1] = l_col

    return s_loc, l_loc


def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """

    index = 0
    rows = []

    for i in matrix:
        search = ""
        for j in i:
            search += j
        if search == word:
            rows.append(index)
        index += 1

    return rows


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """

    transposed = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    return transposed
