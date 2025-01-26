"""
-------------------------------------------------------
Assignment 9, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fv.readline()

    while line != "":
        line = line.strip().split()
        for i in line:
            if i.isalpha():
                hash_set.insert(Word(i.lower()))

        line = fv.readline()

    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """

    total = 0
    max_word = 0

    print(f"""
Using array-based list Hash_Set

Total Comparisons: x,xxx,xxx
Word with maximum comparisons 'www': xx,xxx
    
    """)

    return total, max_word
