"""
-------------------------------------------------------
Lab 5 Functions file
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-17"
-------------------------------------------------------
"""

# CONSTANTS
FRIENDS_1_RATE = 0.05
FRIENDS_2_RATE = 0.10
FRIENDS_3_RATE = 0.15
BURGER = 6.00
WINGS = 8.00
FRIES_COMBO = 1.50
SALAD_COMBO = 2.00


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    if day * month == year:
        magic = True
    else:
        magic = False

    return magic


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """

    if friends == 0:
        final_cost = cost
    elif friends == 1:
        final_cost = cost - (cost * FRIENDS_1_RATE)
    elif friends == 2:
        final_cost = cost - (cost * FRIENDS_2_RATE)
    else:
        final_cost = cost - (cost * FRIENDS_3_RATE)

    return final_cost


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    v1_diff = abs(target - v1)
    v2_diff = abs(target - v2)

    if v1_diff <= v2_diff:
        result = v1
    else:
        result = v2

    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    category = " "

    if 0 < speed < 39:
        category = "Breeze"
    elif 39 <= speed <= 61:
        category = "Strong Wind"
    elif 62 <= speed <= 88:
        category = "Gale Winds"
    elif 89 <= speed <= 117:
        category = "Whole Gale"
    elif speed > 117:
        category = "Hurricane"
    else:
        category = "Unknown"

    return category


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """

    order = input("Order B - burger or W - wings: ")

    if order == "B":
        cost = BURGER
    else:
        cost = WINGS

    combo = input("Make it a combo? (Y/N): ")
    side_cost = 0

    if combo == "Y":
        side = input("Add F - fries or S - salad: ")
        if side == "F":
            side_cost = FRIES_COMBO
        else:
            side_cost = SALAD_COMBO

    price = cost + side_cost

    return price
