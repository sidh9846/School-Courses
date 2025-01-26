/*
 -------------------------------------
 File:    expression.c
 Project: a6
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-20
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expression.h"

/*
 * Convert infix expression string to postfix expression reprsented by queue data structure.
 * @param infixstr - string of infix expression.
 * @return - postfix expression in queue of QUEUE type.
 */
QUEUE infix_to_postfix(char *infixstr) {
// your code
	char *p = infixstr;
	QUEUE queue = { 0 }; // result postfix expression in queue
	STACK stack = { 0 }; // auxiliary stack
	int sign = 1, num = 0;
	NODE *temp = { 0 };
	while (*p) { // expression string traversal
		if (*p == '-' && (p == infixstr || *(p - 1) == '(')) { //get the sign of an operand
			sign = -1;
		} else if (get_type(*p) == 0) { // namely *p is digit character, aation: use horner’s algorithm to get the operand
			num = *p - '0';
			while ((*(p + 1) >= '0' && *(p + 1) <= '9')) {
				num = num * 10 + *(p + 1) - '0';
				p++;
			}
			enqueue(&queue, new_node(sign * num, 0));
			sign = 1;
		} else if (get_type(*p) == 1) {
			// namely *p is an operator character
			while (stack.top
					&& get_priority(*p)
							< get_priority((temp = pop(&stack))->data)) {
				if (temp->type != 2 && temp->type != 3)
					enqueue(&queue, temp);
			}

			if (temp && get_priority(*p) >= get_priority(temp->data)) {
				push(&stack, temp);
			}
			push(&stack, new_node(*p, get_type(*p)));

		} else if (get_type(*p) == 2) {
			// *p == '(‘

			push(&stack, new_node(*p, get_type(*p)));

		} else if (get_type(*p) == 3) {
			// *p == ‘)‘

			while (stack.top && (temp = pop(&stack))->type != 2) {
				enqueue(&queue, temp);
			}

		} // else ignore

		p++; // move to next character
	}
// finally pop each node and insert it to queue
	while (stack.top) {
		enqueue(&queue, pop(&stack));
	}

	return queue;
}

/*
 * Evaluate and return the value postfix expression passed by queue.
 * @parame queue - postfix expression in queue of QUEUE type.
 ^ @return - value of postfix expression
 */
int evaluate_postfix(QUEUE queue) {
// your code
	NODE *p = queue.front;
	STACK stack = { 0 }; //auxilliarystackforpostfixevaluation
	int type = 0;
	while (p) { // traversal the queue linked list
		type = p->type;
		if (type == 0) { // operant
			push(&stack, new_node(p->data, 0));
		} else if (type == 1) { // operator
			int operator = p->data;
			NODE *oprand2 = pop(&stack);
			if (operator == '+') {
				stack.top->data = stack.top->data + oprand2->data;
			} else if (operator == '-') {
				stack.top->data = stack.top->data - oprand2->data;
			} else if (operator == '*') {
				stack.top->data = stack.top->data * oprand2->data;
			} else if (operator == '/') {
				stack.top->data = stack.top->data / oprand2->data;
			}
			free(oprand2);
		}
		p = p->next;
	}
	int result = stack.top->data;
	return result;
}

/*
 * Evaluate and return the value of infix expression passed by string infixstr,
 * using infix_to_postfix() and evaluate_postfix() functions.
 * @param infixstr - string of infix expression.
 * @return - value of the infix expression.
 */
int evaluate_infix(char *infixstr) {

	// 1. call infix_to_postfix() compute the postfix expression queue
	QUEUE q = infix_to_postfix(infixstr);

	int result = evaluate_postfix(q);

	return result;
}
