"""
-------------------------------------------------------
Midterm A Task 3 Function Definitions
-------------------------------------------------------
Author: Manveer Sidhu
ID:     169029846
Email:  sidh9846@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
BASE_COST = 45.00
COST_PER_DLC = 5.00
VIP_DISCOUNT = 0.10
# your code here


def video_game_purchase():
    """
    -------------------------------------------------------
    Determines the cost of a video game. The cost is made up of:
        base cost: $45.00
        cost per DLC (DownLoadable Content): $5.00
        VIP discount 10% only if:
            more than 1 DLCs purchased
            and purchaser is a VIP
    Use: cost = video_game_purchase()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​​‌‌​​​​‌‌​‌​‌‌​:
        cost - cost of a video game based upon the base game,
            the number of DLCs purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    dlc_purchased = int(input("How many DLCs are you purchasing? "))
    dlc_cost = dlc_purchased * COST_PER_DLC
    cost = 0

    if dlc_purchased > 1:
        vip = input("Are you a VIP member (Y/N)? ")
        if vip == "Y":
            dlc_cost = dlc_purchased * COST_PER_DLC
            cost = BASE_COST + dlc_cost - \
                ((BASE_COST + dlc_cost) * VIP_DISCOUNT)
        if vip == "N":
            dlc_cost = dlc_purchased * COST_PER_DLC
            cost = BASE_COST + dlc_cost
    elif dlc_purchased == 1:
        dlc_cost = dlc_purchased * COST_PER_DLC
        cost = BASE_COST + dlc_cost
    else:
        cost = BASE_COST

    return cost
