"""
-------------------------------------------------------
Assignment 8, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

# constants
CHAR_ALLOWED = "1234567890-"
NUMBERS = "1234567890"


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    string_lst = []
    indexs = []
    shift = 0

    for i in string:
        string_lst.append(i)

    for i in range(1, len(string_lst)):
        if string_lst[i] == string_lst[i].upper() and string_lst[i].isalpha():
            indexs.append(i)

    for i in indexs:
        string_lst.insert(i + shift, " ")
        shift += 1

    new_string = "".join(string_lst).lower().capitalize()

    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """

    if string[-1:] == "s" or string[-2:] == "sh" or string[-2:] == "ch":
        plural = string + "es"
    elif string[-1:] == "y" and string[-2:] != "ay" and string[-2:] != "oy":
        plural = string.replace(string[-1:], "ies")
    else:
        plural = string + "s"

    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """

    common = ""

    if len(string1) >= len(string2):
        str1 = string1
        str2 = string2
    else:
        str1 = string2
        str2 = string1

    for i in range(1, len(str1)):
        if str1[-i] == str2[-i]:
            common = common + str1[-i]
        else:
            break

    common = common[::-1]

    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True
    last_char = ""
    groups = 0

    # - it consists of only digits and dashes ('-')
    for i in isbn:
        if i not in CHAR_ALLOWED:
            valid = False

    # - it contains 5 groups of digits separated by dashes
    for i in isbn:
        if last_char in NUMBERS and i == "-":
            groups += 1
        last_char = i

    if groups != 4:
        valid = False

    # - its first group of digits is either '978' or '979'
    if isbn[0:3] != "978" and isbn[0:3] != "979":
        valid = False

    # - its final group of digits is a single digit
    if isbn[-2] != "-":
        valid = False

    # - its entire length is 17 characters
    if len(isbn) != 17:
        valid = False

    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    old_word = word_list[0]

    for i in range(1, len(word_list)):
        new_word = word_list[i]
        if old_word[-1] == new_word[0]:
            word_chain = True
        else:
            word_chain = False
            break
        old_word = new_word

    return word_chain
