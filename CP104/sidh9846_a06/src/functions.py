"""
-------------------------------------------------------
Assignment 6, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    Determines the score of game series given the winner of 
    each game.
    Use: winner()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        blue - Score of blue team in series (int)
        grey - Score of grey team in series (int)
    ------------------------------------------------------
    """
    team = "none"
    blue = 0
    grey = 0

    while team != "":
        team = input("Enter the winning team: ")
        if team == "blue":
            blue += 1
        elif team == "grey":
            grey += 1

    return blue, grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    prime = True
    i = 1

    if num == 1:
        prime = False
    else:
        while i <= num:
            if num % i == 0 and i != 1 and i != num:
                prime = False
            i += 1

    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    balance = principal
    month = 0
    month_rate = rate / 1200
    interest = 0

    print(f"Principal:   ${principal:.2f}")
    print(f"Interest rate : {rate:.1f}%")
    print(f"Monthly payment: ${payment:.2f}")

    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while balance > 0:
        month += 1
        interest = month_rate * balance
        if payment > balance:
            payment = balance + interest
            balance = 0
        else:
            balance = balance + interest - payment

        print(f"{month:5}{interest:9.2f}{payment:10.2f} {balance:9.2f}")

    return


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """

    i = 0
    result = 1
    if num == 0:
        i = 2
    else:
        while result != 0:
            result = num // (10 ** i)
            i += 1

    i -= 1

    return i


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """

    i = 1
    factors = 0

    while i < num:
        if num % i == 0:
            factors = factors + i
        i += 1

    return factors
