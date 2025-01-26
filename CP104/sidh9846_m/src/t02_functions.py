"""
-------------------------------------------------------
Midterm A Task 2 Function Definitions
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""


def chess_rating(points):
    """
    -------------------------------------------------------
    Determines the rating given chess game win/lose/draw points.
        If points is 2700 or greater, the rating is "Super Grandmaster".
        If points is 2500 or greater but less than 2700, the rating is "Grandmaster".
        If points is 2200 or greater but less than 2500, the rating is "Master".
        If points is 1200 or greater but less than 2200, the rating is "Class A-D".
        If points is 0 or greater but less than 1200, the rating is "Novice".
        If points is less than 0, return "Error"
    Use: rating = chess_rating(points)
    -------------------------------------------------------
    Parameters:
        points - win/loss/draw points (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        rating - description of chess rating (str)
    -------------------------------------------------------
    """

    # your code here
    if points >= 2700:
        rating = "Super Grandmaster"
    elif points >= 2500:
        rating = "Grandmaster"
    elif points >= 2200:
        rating = "Master"
    elif points >= 1200:
        rating = "Class A-D"
    elif points >= 0:
        rating = "Novice"
    else:
        rating = "Error"

    return rating
