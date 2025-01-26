/**
 * -------------------------------------
 * @file  strings_length.c
 * Lab 4 Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-02-03
 *
 * -------------------------------------
 */
#include "functions.h"

void strings_length(strings_array *data, FILE *fp_short, FILE *fp_long,
		int length) {

	// your code here

	for (int i = 0; i < data->lines; i++) {
		char *currStr = data->strings[i];

		int len = strlen(currStr);

		if (len < length) {
			fprintf(fp_short, currStr);
			fprintf(fp_short, "\n");
		} else {
			fprintf(fp_long, currStr);
			fprintf(fp_long, "\n");
		}
	}
}
