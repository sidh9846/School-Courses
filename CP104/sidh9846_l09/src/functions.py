"""
-------------------------------------------------------
Lab 9, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-17"
-------------------------------------------------------
"""
# Constants
VOWEL = "AEIOUaeiou"
NUMBERS = "1234567890"


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """

    test = url
    url_type = ""

    if test[-3:] == "com":
        url_type = "business"
    elif test[-3:] == "org":
        url_type = "non-profit"
    else:
        url_type = "other"

    return url_type


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    pc = product_code[:3]
    pi = product_code[3:7]
    pq = product_code[7:]

    return pc, pi, pq


def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """

    counter = 0

    for i in s:
        if i in NUMBERS:
            counter += 1

    return counter


def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(sstring)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with its vowels removed (str)
    -------------------------------------------------------
    """

    out = ""

    for i in range(len(string)):
        if string[i] not in VOWEL:
            out = out + string[i]

    return out


def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """

    num1 = int(expr[0])
    opp = expr[2]
    num2 = int(expr[4])

    if opp == "+":
        result = num1 + num2
    elif opp == "-":
        result = num1 - num2
    elif opp == "*":
        result = num1 * num2
    elif opp == "/" or opp == "%":
        if num2 == 0:
            result = None
        elif opp == "/":
            result = num1 / num2
        elif opp == "%":
            result = num1 % num2

    return result
