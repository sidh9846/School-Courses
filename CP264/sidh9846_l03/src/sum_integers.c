/**
 * -------------------------------------
 * @file  sum_integers.c
 * Lab 3 Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-25
 *
 * -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "functions.h"

int sum_integers(void) {

	// your code here

	char input[STRING_BIG];
	int number;
	int count;

	printf("Enter integers, one per line:\n");

	while (fgets(input, sizeof(input), stdin)) {
		if (sscanf(input, "%d", &number) == 1) {
			count += number;
		} else {
			break;
		}
	}

	return count;
}
