"""
-------------------------------------------------------
Assignment 3, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

# Imports
from enum import Enum
from Stack_array import Stack

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """

    target1_temp = Stack()
    target2_temp = Stack()

    count = 0

    while not source.is_empty():
        target1_temp.push(source.pop())
        count += 1
        if not source.is_empty():
            target2_temp.push(source.pop())
            count += 1

    if count % 2 == 0:
        target1 = target2_temp
        target2 = target1_temp
    else:
        target1 = target1_temp
        target2 = target2_temp

    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    stack = Stack()
    palindrome = True
    string_new = ""

    for i in string:
        if i.isalpha():
            string_new += i.lower()

    length = len(string_new)

    if length % 2 != 0:
        x = 1
    else:
        x = 0

    for i in range(length // 2):
        stack.push(string_new[i])

    for i in string_new[(length//2) + x:]:
        if stack.pop().lower() != i.lower():
            palindrome = False
        else:
            pass

    return palindrome


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    stack = Stack()

    postfix = string.split()

    for i in postfix:
        if i.isnumeric():
            stack.push(i)
        elif i in OPERATORS:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            if i == "+":
                stack.push(num1 + num2)
            elif i == "-":
                stack.push(num1 - num2)
            elif i == "*":
                stack.push(num1 * num2)
            elif i == "/":
                stack.push(num1 / num2)

    answer = stack.pop()

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """

    stack = Stack()

    path = []

    key = 'Start'
    value = maze[key]
    [stack.push(i) for i in value]

    while not stack.is_empty():
        path.append(stack.pop())
        if path[-1] != "X":
            key = path[-1]
            value = maze[key]
            if "X" in value:
                path.append("X")
                break
            [stack.push(i) for i in value]
        elif path[-1] == "X":
            break

    return path


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    # INIT
    stack = Stack()
    is_mirror = True
    index = 0

    # CHECKS FOR INVAILD CHARS
    for i in string:
        if i not in m and i not in valid_chars:
            mirror = MIRRORED.INVALID_CHAR
            is_mirror = False

    # CHECKS IF MIRROR CHAR IN STR
    if is_mirror:
        if m not in string:
            mirror = MIRRORED.NOT_MIRRORED
            is_mirror = False

    # PUTS FIRST HALF OF STR INTO STACK UNTILL M CHAR
    if is_mirror:
        for i in string:
            if i != m:
                stack.push(i)
                index += 1
            else:
                break

    # INIT LEN OF STACK AND STR
    length_stack = index
    index += 1
    length_string = len(string[index:])

    # CHECKS IF THERE IS AN INBALANCE
    if is_mirror:
        if length_stack > length_string:
            mirror = MIRRORED.TOO_MANY_LEFT
            is_mirror = False
        elif length_stack < length_string:
            mirror = MIRRORED.TOO_MANY_RIGHT
            is_mirror = False

    # CHECKS IF IT IS A MIRROR
    if is_mirror:
        for i in string[index:]:
            if i == stack.pop():
                pass
            else:
                mirror = MIRRORED.MISMATCHED
                is_mirror = False
                break

    # IS MIRROR
    if is_mirror:
        mirror = MIRRORED.IS_MIRRORED

    return mirror
