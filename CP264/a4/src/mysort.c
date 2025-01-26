/*
 -------------------------------------
 File:    mysort.c
 Project: a4
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-09
 -------------------------------------
 */

#include "mysort.h"

/**
 * Use selection sort algorithm to sort array of float pointers such that their pointed values are incresing order.
 *
 * @param *a[] - array of float pointers.
 * @param left - the start index of float pointer in array.
 * @param right - the end index of float pointer in array
 */
void select_sort_inc(float *a[], int left, int right) {

	int i, j, k;
	float *temp;
	int n = right;

	for (i = left; i < n; ++i) {
		k = i;
		for (j = i + 1; j <= n; ++j) {
			if (*a[j] < *a[k]) {
				k = j;
			}
		}
		if (i != k) { // the following swap a[i] and a[k] temp = a[k];
			temp = a[k];
			a[k] = a[i];
			a[i] = temp;
		}
	}
}

/**
 * Use quick sort algorithm to sort array of float pointers such that their pointed values are incresing order.
 *
 * @param *a[] - array of float pointers.
 * @param left - the start index of float pointer in array.
 * @param right - the end index of float pointer in array
 */
void quick_sort_inc(float *a[], int left, int right) {
	int i, j;
	float key, *temp;
	if (left < right) {
		key = *a[left];
		i = left + 1;
		j = right;
		while (i <= j) {
			while (i <= right && *a[i] <= key)
				i++;
			while (j >= left && *a[j] > key)
				j--;
			if (i < j) {
				//swap a[i] and a[j]
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}

		// swap a[left] and a[j];
		temp = a[left];
		a[left] = a[j];
		a[j] = temp;

		quick_sort_inc(a, left, j - 1);
		quick_sort_inc(a, j + 1, right);
	}
}
