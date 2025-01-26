/*
 -------------------------------------
 File:    mystring.c
 Project: a3
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-02
 -------------------------------------
 */

#include "mystring.h"

/**
 * Count the number words of given simple string. A word starts with an
 * English charactor end with a charactor of space, tab, comma, or period.
 *
 * @param s - char pointer to a str
 * @return - return the number of words.
 */
int str_words(char *s) {

	int index = 0;
	char currLetter = *s;
	char nextLetter;
	int count = 0;

	while (currLetter != 0) {

		// if current letter is a letter
		if ((65 <= currLetter && currLetter <= 90)
				|| (97 <= currLetter && currLetter <= 122)) {

			// get next letter
			nextLetter = *(s + index + 1);

			// end case
			if (nextLetter == 0) {
				return ++count;
			} else if (nextLetter == 32 || nextLetter == 9 || nextLetter == 44
					|| nextLetter == 46) {
				count++;
			}
		}

		index++;
		currLetter = *(s + index);
	}

	return count;
}

/**
 * Change every upper case English letter to its lower case of string passed by s
 *
 * @param s - char pointer to a str
 * @return - return the number of actual flips.
 */
int str_lower(char *s) {
	int index = 0;
	char currLetter = *s;
	int count = 0;

	while (currLetter != 0) {
		if ((65 <= currLetter && currLetter <= 90)) {
			*(s + index) = currLetter + 32;
			count++;
		}
		index++;
		currLetter = *(s + index);
	}

	return count;
}

/**
 * Remove unnecessary space characters in a simple string passed by `s`
 *
 * @param s - char pointer to a str
 */
void str_trim(char *s) {

	char *p = s;
	char *t = s;
	int spaces;

	if (s[0] == 0) {
		return;
	}

	while (*p && *p == 32) {
		p++;
	}

	while (*p) {
		if (*p != 32) {
			*t = *p;
			t++;
			spaces = 0;
		} else if (spaces == 0) {
			*t = 32;
			t++;
			spaces = 1;
		}
		p++;
	}

	if (t > s && *(t - 1) == 32) {
		*(t - 1) = 0;
	} else {
		*t = 0;
	}

}

