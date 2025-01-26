/**
 * -------------------------------------
 * @file  factorial.c
 * factorial function file
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-11
 *
 * -------------------------------------
 */

#include "factorial.h"

/**
 * Compute the factorial n! and does overflow detection.
 *
 * @param n - a positive integer value
 * @return -  the factorial n! if it is not overflow; otherwise 0.
 */
int factorial(int n) {

	int result = 1;
	int temp;

	for (int i = 2; i <= n; i++) {
		temp = result * i;
		if (temp / result != i) {
			return 0;
		} else {
			result *= i;
		}
	}

	return result;

}
