/*
 -------------------------------------
 File:    fibonacci.c
 Project: a2
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-01-23
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include "fibonacci.h"

/**
 * Computes and returns the nth Fibonacci number F(n) using recursive algorithm
 */
int recursive_fibonacci(int n) {
// your code

	if (n < 0) {
		return -3;
	} else if (n <= 1) {
		return n;
	} else {
		return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
	}
}

/**
 * Computes and returns the nth Fibonacci number F(n) using iterative algorithm
 */
int iterative_fibonacci(int n) {
// your code

	if (n < 0) {
		return -3;
	} else if (n <= 1) {
		return n;
	} else {

		int prev = 1;
		int result = 1;
		int temp;

		for (int i = 2; i < n; i++) {
			temp = result;
			result += prev;
			prev = temp;

			if (result < temp) {
				return -2;
			}
		}

		return result;
	}
}

/**
 *  computes and returns the nth Fibonacci number F(n) using using dynamic programming
 *  bottom-up method with external array f[n+1] of initial value -1 for all elements.
 */
int dpbu_fibonacci(int *f, int n) {
// your code

	for (int i = 0; i < n; i++) {
		*(f + i) = iterative_fibonacci(n);
	}

	return *(f);
}

/**
 * Computes and returns the Fibonacci number F(n) using dynamic programming top-down
 * method with external array f[n+1] of initial value -1 for all elements.
 */
int dptd_fibonacci(int *f, int n) {
// your code

	if (n <= 0) {
		return n;
	} else {
		for (int i = 0; i < n; i++) {
			int temp = recursive_fibonacci(n);
			*(f + i) = temp;
		}

		return *(f);
	}
}
