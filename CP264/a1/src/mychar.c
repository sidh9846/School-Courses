/**
 * -------------------------------------
 * @file  mychar.c
 * mychar functions
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-11
 *
 * -------------------------------------
 */

#include "mychar.h"

/**
 * Determine the type of a char character.
 *
 * @param c - char type value
 * @return - 0 if c is a digit, 1 if c is an arithmetic operator, 2 if c is an English letter; otherwise -1.
 */
int mytype(char c) {

	int ascii = (int) c;

	if ((48 <= ascii) && (ascii <= 57)) {
		return 0;
	} else if (ascii == 42 || ascii == 43 || ascii == 45 || ascii == 47) {
		return 1;
	} else if (((65 <= ascii) && (ascii <= 90))
			|| ((97 <= ascii) && (ascii <= 122))) {
		return 2;
	} else {
		return -1;
	}
}

/**
 * Flip the case of an English character.
 *
 * @param c - char type value of ASCII code of English letter.
 * @return  -  c's upper/lower case letter if c is a lower/upper case English letter.
 */
char case_flip(char c) {

	int ascii = (int) c;

	if ((65 <= ascii) && (ascii <= 90)) {
		return ((char) (ascii + 32));
	} else if ((97 <= ascii) && (ascii <= 122)) {
		return ((char) (ascii - 32));
	} else {
		return -1;
	}
}

/**
 * Convert digit character to the corresponding integer value.
 *
 * @param c - char type value of ASCII code of digit charactor.
 * @return - its corresponding integer value if c is a digit character.
 */
int char_to_int(char c) {

	int ascii = (int) c;

	if ((48 <= ascii) && (ascii <= 57)) {
		return ((int) ascii - 48);
	} else {
		return -1;
	}
}
