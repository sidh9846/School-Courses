/**
 * -------------------------------------
 * @file  mychar.h
 * mychar header file
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-11
 *
 * -------------------------------------
 */

#ifndef MYCHAR_H_
#define MYCHAR_H_

/**
 * Determine the type of a char character.
 *
 * @param c - char type value
 * @return - 0 if c is a digit, 1 if c is an arithmetic operator, 2 if c is an English letter; otherwise -1.
 */
int mytype(char c);

/**
 * Flip the case of an English character.
 *
 * @param c - char type value of ASCII code of English letter.
 * @return  -  c's upper/lower case letter if c is a lower/upper case English letter.
 */
char case_flip(char c);

/**
 * Convert digit character to the corresponding integer value.
 *
 * @param c - char type value of ASCII code of digit charactor.
 * @return - its corresponding integer value if c is a digit character.
 */
int char_to_int(char c);

#endif /* MYCHAR_H_ */
