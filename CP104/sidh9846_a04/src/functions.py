"""
-------------------------------------------------------
Assignment 4, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-10-27"
-------------------------------------------------------
"""


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing
    the corresponding day of the week.
    Returns "Error" if day_number is outside the range of 1-7.
    Use: day = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - day of the week represented by a number (int)
    Returns:
        day - day of the week (str)
    ------------------------------------------------------
    """
    if day_number == 1:
        day = "Monday"
    elif day_number == 2:
        day = "Tuesday"
    elif day_number == 3:
        day = "Wednesday"
    elif day_number == 4:
        day = "Thursday"
    elif day_number == 5:
        day = "Friday"
    elif day_number == 6:
        day = "Saturday"
    elif day_number == 7:
        day = "Sunday"
    else:
        day = "Error"

    return day


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """

    if aqi < 0:
        level = "Error"
    elif aqi < 51:
        level = "Good"
    elif aqi < 101:
        level = "Moderate"
    elif aqi < 151:
        level = "Unhealthy for Sensitive Groups"
    elif aqi < 201:
        level = "Unhealthy"
    elif aqi < 301:
        level = "Very Unhealthy"
    else:
        level = "Hazardous"

    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """

    if v2 >= v1 and v3 >= v1:
        product = v2 * v3
    elif v1 >= v2 and v3 >= v2:
        product = v1 * v3
    else:
        product = v1 * v2

    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """

    if rgb1 == "red":
        if rgb2 == "red":
            colour = "red"
        elif rgb2 == "blue":
            colour = "fuchsia"
        elif rgb2 == "green":
            colour = "yellow"
        else:
            colour = "Error"

    elif rgb1 == "blue":
        if rgb2 == "red":
            colour = "fuchsia"
        elif rgb2 == "blue":
            colour = "blue"
        elif rgb2 == "green":
            colour = "aqua"
        else:
            colour = "Error"

    elif rgb1 == "green":
        if rgb2 == "red":
            colour = "yellow"
        elif rgb2 == "blue":
            colour = "aqua"
        elif rgb2 == "green":
            colour = "green"
        else:
            colour = "Error"
    else:
        colour = "Error"

    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns one of the following strings:
    - "Yee" if number is evenly divisible by 3
    - "Ha" if number is evenly divisible by 7
    - "Yee Ha" if number is evenly divisible by both 3 and 7
    - "Nada" if number is none of the above
    Use: yee_ha = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - number to be tested (int)
    Returns:
        result - the result based on the number tested (str)
    ------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        result = "Yee Ha"
    elif number % 3 == 0:
        result = "Yee"
    elif number % 7 == 0:
        result = "Ha"
    else:
        result = "Nada"

    return result
