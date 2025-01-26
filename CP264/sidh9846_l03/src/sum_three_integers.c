/**
 * -------------------------------------
 * @file  functions.c
 * Lab 2 Functions Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2023-09-09
 *
 * -------------------------------------
 */
#include "functions.h"

int sum_three_integers(void) {

	// your code here

	char input[STRING_BIG];
	int num1;
	int num2;
	int num3;

	while (1) {
		printf("Enter three comma-separated integers: ");
		fgets(input, sizeof input, stdin);
		if (sscanf(input, "%d,%d,%d", &num1, &num2, &num3) != 3) {
			printf("The integers were not properly entered.\n");
		} else {
			break;
		}
	}

	return num1 + num2 + num3;

}
