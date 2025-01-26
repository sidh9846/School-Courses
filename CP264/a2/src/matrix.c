/*
 -------------------------------------
 File:    matrix.c
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
#include <math.h>
#include "matrix.h"

/**
 *
 * Compute and return the norm of vector v, namely, the square root of the sum of
 * squares of elements of v.
 *
 * @param v - the address of first the vector array.
 * @param n - the length of vector v.
 * @return - the norm of vector v.
 *
 */
float norm(float *v, int n) {
// your code

	float total;

	for (int i = 0; i < n; i++) {
		total += pow(*(v + i), 2);
	}

	return sqrt(total);

}

/**
 * Compute and return the dot product of vectors v1[n] and v2[n], namely the sum of product of corresponding elements of v1 and v2.
 *
 * @param v1 - the address of the first vector array.
 * @param v2 - the address of the second vector array.
 * @param n - the length of vector v1 and v2.
 * @return -  the value of dot product of v1 and v2.
 */
float dot_product(float *v1, float *v2, int n) {
// your code

	float total;

	for (int i = 0; i < n; i++) {
		total += *(v1 + i) * *(v2 + i);
	}

	return total;
}

/**
 * Compute the multiplication of two n by matrices.
 * @param m1 - the address of the first matrix array.
 * @param m2 - the address of the second matrix array.
 * @param m3 - the address of the output matrix array.
 * @param n - the row and colum size of m1 and m2.
 */
void matrix_multiply_matrix(float *m1, float *m2, float *m3, int n) {
// your code

	float s = 0;
	int i, j, k;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			s = 0;
			for (k = 0; k < n; k++) {
				s += *(m1 + i * n + k) * *(m2 + k * n + j);
			}
			*(m3 + i * n + j) = s;
		}
	}
}

/**
 * Compute the multiplication of matrix and vector.
 * @param m - the address of the first matrix array.
 * @param v - the address of the vector array.
 * @param vout - the address of the output vector array.
 * @param n - the length of vector v.
 */
void matrix_multiply_vector(float *m, float *vin, float *vout, int n) {
// your code

	float s;
	for (int i = 0; i < n; i++) {
		s = 0;
		for (int j = 0; j < n; j++) {
			s += *(vin + j) * *(m + i * n + j);
		}
		*(vout + i) = s;
	}

}
