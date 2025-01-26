"""
-------------------------------------------------------
Assignment 1, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-01-24"
-------------------------------------------------------
"""

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    cleaned = []

    for i in values:
        if i not in cleaned:
            cleaned.append(i)

    values.clear()

    for i in cleaned:
        values.append(i)

    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    line = fv.readline()

    while line != "":
        for i in line:
            if i == i.upper() and i.isalpha():
                u += 1
            elif i == i.lower() and i.isalpha():
                l += 1
            elif i.isnumeric():
                d += 1
            elif i == " ":
                w += 1
            else:
                r += 1
        line = fv.readline()

    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """

    locations = []
    index = 0
    gap = 0

    while index != -1:
        index = string.find(sub)
        string = string[index+1:]
        if index != -1:
            locations.append(index + gap)
        gap = gap + index + 1

    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    leap_year = False

    if year % 400 == 0:
        leap_year = True
    elif year % 4 == 0 and year % 100 != 0:
        leap_year = True

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True

    if not name[0].isalpha():
        valid = False
    else:
        for i in name:
            if i not in ALLOWED_CHARS:
                valid = False

    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    transposed = []
    rows = len(a)
    cols = len(a[0])

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(a[j][i])
        transposed.append(new_row)

    return transposed


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """

    rows = len(a)
    col = len(b[0])

    p = len(b)

    c = []

    for i in range(rows):
        newline = []
        for j in range(col):
            newline.append(0)
        c.append(newline)

    for i in range(rows):
        for j in range(col):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]

    return c


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """

    VOWELS = "aeiouyAEIOUY"
    index = 0
    pl = ""

    if word[0] in VOWELS:
        pl = word + "way"
    else:
        for i in word:
            if i not in VOWELS:
                index += 1
            else:
                break

        pl = word[index:] + word[:index].lower() + "ay"

    if word[0] == word[0].upper():
        temp = pl[0].upper()
        pl = temp + pl[1:]

    return pl


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """

    estring = ""
    index = 0

    for i in string:
        if i.upper() in ALPHA:
            alpha_index = ALPHA.find(i.upper())
            alpha_index = alpha_index + n
            if alpha_index > len(ALPHA) - 1:
                alpha_index %= len(ALPHA)
            estring += ALPHA[alpha_index]
        else:
            estring += string[index]

        index += 1

    return estring
