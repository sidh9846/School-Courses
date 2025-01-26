/*
 -------------------------------------
 File:    polynomial.c
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
#include "polynomial.h"

#define EPSILON 1e-6

/**
 *   Computes and returns the value of the following polynomial p(x)
 *   of order n and coefficients p[0], …, p[n-1], namely
 */
float horner(float *p, int n, float x) {
// your code

	float r = 0;
	for (int i = 0; i < n; i++) {
		r = r * x + p[i];
	}
	return r;
}

/**
 *  Finds an approximate real root c in interval [a, b] of polynomial P(x),
 *  using the bisection method.
 */
float bisection(float *p, int n, float a, float b) {
// your code

	float c;

	while ((b - a) >= EPSILON) {

		float c = (a + b) / 2;

		if (fabs(horner(p, n, c)) < EPSILON || fabs(c - a) < EPSILON) {
			return c;
		} else if ((horner(p, n, c) * horner(p, n, a)) >= 0) {
			a = c;
		} else {
			b = c;
		}
	}

	return c;
}
