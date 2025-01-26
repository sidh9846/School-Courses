/**
 * -------------------------------------
 * @file  strings_with_substring.c
 * Lab 4 Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-02-03
 *
 * -------------------------------------
 */
#include "functions.h"

void strings_with_substring(strings_array *data, char *substr) {

	// your code here

	for (int i = 0; i < data->lines; i++) {
		char *currStr = data->strings[i];

		if (strstr(currStr, substr) != NULL) {
			printf("%s\n", currStr);
		}
	}

}
