"""
-------------------------------------------------------
Lab 10, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    count = -1

    while count != n:
        result = fh.readline().strip().split(",")
        count += 1

    if result == [""]:
        result = []

    return result


def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """

    line = fh.readline()
    early_date = "9999-99-99"
    result = line

    while line != "":
        date = line[-11:].strip()
        if date < early_date:
            early_date = date
            result = line.strip()
        line = fh.readline()

    result = result.split(",")

    return result


def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """

    line = fh.readline()
    num = line.strip()

    while line != "":
        num = line.strip()
        line = fh.readline()

    num = int(num)
    num += 1

    fh.write(f"{num}\n")

    return num


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """

    line = fh.readline()
    shortest = line

    while line != '':
        if len(shortest) > len(line.strip()):
            shortest = line.strip()
        line = fh.readline()

    return shortest


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(n):
        fh_2.write(fh_1.readline())

    return
