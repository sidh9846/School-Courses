"""
-------------------------------------------------------
Lab 5, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)

    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)

    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"

    index = 0
    count = 0

    if index != len(s):
        if s[index].lower() in vowels:
            count += 1
            index += 1
            count += vowel_count(s[index:])
        else:
            index += 1
            count += vowel_count(s[index:])

    #print(index, count)
    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """

    if power == 1:
        ans = base
    elif power == 0:
        ans = 1
    elif power < 0:
        ans = 1/base * to_power(base, power + 1)
    else:
        ans = base * to_power(base, power - 1)

    ans = float(ans)

    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    palindrome = True

    if len(s) > 0:
        if not s[0].isalpha():
            palindrome = is_palindrome(s[1:])
        elif not s[-1].isalpha():
            palindrome = is_palindrome(s[:-1])
        elif s[0].lower() != s[-1].lower():
            palindrome = False
        else:
            palindrome = is_palindrome(s[1:-1])

    return palindrome


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """

    if bag == []:
        new_set = []
    elif bag[-1] in bag[:-1]:   # if last char in the rest of the string
        new_set = bag_to_set(bag[:-1])      # do not add // return same string
    else:
        # if not in rest of string, add to end of string
        new_set = bag_to_set(bag[:-1]) + [bag[-1]]
    return new_set


'''
    temp = []
    index = 0
    new_set = []

    if index != len(bag) and bag[index] in temp:
        pass
    else:
        temp.append(bag[index])
        new_set.append(bag[index])
        index += 1
        print(index)
        bag = bag_to_set(bag[index:])
'''
