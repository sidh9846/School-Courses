/*
 -------------------------------------
 File:    bigint.c
 Project: a5
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-15
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include "bigint.h"

/*
 * Creates and returns BIGINT object by converting the digit string.
 */
BIGINT bigint(char *digitstr) {
	BIGINT bn = { 0 };
	if (digitstr == NULL)
		return bn;
	else if (!(*digitstr >= '0' && *digitstr <= '9')) { // not begin with digits
		return bn;
	} else if (*digitstr == '0' && *(digitstr + 1) == '\0') { // just "0"
		dll_insert_end(&bn, new_node(*digitstr - '0'));
		return bn;
	} else {
		while (*digitstr) {
			if (*digitstr >= '0' && *digitstr <= '9') {
				dll_insert_end(&bn, new_node(*digitstr - '0'));
			} else {
				dll_clean(&bn);
				break;
			}
			digitstr++;
		}
		return bn;
	}
}

/*
 * Add two BIGINT operants and returns the sum in BIGINT type.
 * @param oprand1  - first operand of BIGINT type.
 * @param oprand2  - second operand of BIGINT type.
 * @return - the sum of oprand1 and oprand2 in BIGINT type.
 */
BIGINT bigint_add(BIGINT oprand1, BIGINT oprand2) {
	BIGINT sum = bigint(NULL);
	NODE *p1 = oprand1.end;
	NODE *p2 = oprand2.end;
	int c = 0, a, b, s;
	while (p1 || p2) {
		a = 0;
		b = 0;
		if (p1) {
			a = p1->data;
			p1 = p1->prev;
		}
		if (p2) {
			b = p2->data;
			p2 = p2->prev;
		}
		// compute the sum digit s and insert it at start of the doubly linked list
		s = 0;
		s = a + b + c;
		if (s >= 10) {
			c = 1;
			s -= 10;
		} else {
			c = 0;
		}
		dll_insert_start(&sum, new_node(s));
	}
	if (c == 1) {
		// insert 1 at start of the doubly linked list
		dll_insert_start(&sum, new_node(1));
	}
	return sum;
}

/*
 * Compute and return Fibonacci(n)
 * @param n - input positive integer
 * @return  - Fibonacci(n) in BIGINT type
 */
BIGINT bigint_fibonacci(int n) {
	BIGINT f1 = bigint("0");
	BIGINT f2 = bigint("1");
	BIGINT temp = bigint(NULL);
	if (n == 0) {
		return f1;
	} else if (n == 1) {
		return f2;
	} else {
		for (int i = 2; i <= n; i++) {
			temp = f2;
			f2 = bigint_add(f1, f2);
			f1 = temp;
		}
		dll_clean(&f1);
		return f2;
	}
}
