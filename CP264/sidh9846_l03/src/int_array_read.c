/**
 * -------------------------------------
 * @file  int_array_read.c
 * Lab 3 Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-25
 *
 * -------------------------------------
 */
#include "functions.h"

void int_array_read(int *array, int size) {

	// your code here

	int count = 0;
	char input[STRING_BIG];
	float number;

	printf("Enter 4 values for an array of int.\n");

	while (count < size) {
		printf("Value for index %d: ", count);

		fgets(input, sizeof(input), stdin);

		if (sscanf(input, "%f", &number) == 1) {
			array[count] = number;
			count++;
		} else {
			printf("Not a valid integer\n");
		}
	}
}
