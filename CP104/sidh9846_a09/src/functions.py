"""
-------------------------------------------------------
Assignment 9, Functions File
-------------------------------------------------------
Author:  Manveer Sidhu
ID:      169029846
Email:   sidh9846@mylaurier.ca
__updated__ = "2022-12-01"
-------------------------------------------------------
"""


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    count = 0

    while count != linecount:
        line = fh.readline().strip()
        print(line)
        count += 1

    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """

    numbers = []

    line = fh.readline().strip()

    while line != "":
        line_lst = line.split(",")
        for i in line_lst:
            if i.isnumeric():
                numbers.append(int(i))
        line = fh.readline().strip()

    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """

    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0

    line = fh.readline()

    while line != "":
        for i in line:
            if i == i.upper() and i.isalpha():
                ucount += 1
            elif i == i.lower() and i.isalpha():
                lcount += 1
            elif i.isnumeric():
                dcount += 1
            elif i == " ":
                wcount += 1
        line = fh.readline()

    return ucount, lcount, dcount, wcount


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """

    line = fh_in.readline()
    count = 0

    while line != "":
        new_line = (f"[{count}]" + f" {line}")
        count += 1
        fh_out.write(new_line)
        line = fh_in.readline()

    return


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """

    line = students.readline().strip()

    count = 0
    lowest = 101
    highest = -1
    total_grade = 0

    while line != "":
        info = line.split(",")
        grade = int(info[3])
        id = info[2]
        total_grade += grade
        if grade < lowest:
            lowest = grade
            l_id = id
        if grade > highest:
            highest = grade
            h_id = id

        count += 1
        line = students.readline().strip()

    avg = total_grade / count

    return l_id, h_id, avg
