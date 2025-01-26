"""
-------------------------------------------------------
Lab 5, Task 3
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-02-14"
-------------------------------------------------------
"""

from functions import vowel_count


s = input("Enter string: ")


def test(s):
    vowels = "aeiou"
    count = 0

    for c in s:
        if c.lower() in vowels:
            count = count + 1

    return count


# print(test(s))
count = vowel_count(s)

print(f"There are {count} vowel(s) in '{s}'")
