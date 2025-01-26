/**
 * -------------------------------------
 * @file  by_ptr.c
 * Lab 2 Pointer Functions Source Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-06
 *
 * -------------------------------------
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "by_ptr.h"

void fill_values_by_ptr(int *values, int size) {

	for (int i = 0; i < size; i++) {
		*(values + i) = i + 1;
	}
}

void fill_squares_by_ptr(int *values, long int *squares, int size) {

	// your code here

	for (int i = 0; i < size; i++) {
		float square = pow(*(values + i), 2);
		*(squares + i) = square;
	}

}

void print_by_ptr(int *values, long int *squares, int size) {

	// your code here

	printf("Value  Square\n");
	printf("-----  ----------\n");

	for (int i = 0; i < size; i++) {
		printf("%5li %11li\n", *(values + i), *(squares + i));
	}

}
