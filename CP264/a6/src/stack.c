/*
 -------------------------------------
 File:    stack.c
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
#include "stack.h"

/*
 * Push a node into a linked list stack
 * @param STACK *sp - pointer to the stack
 * @param NODE *np - pointer to the node.
 */
void push(STACK *sp, NODE *np) {
// your code

	if (sp->length == 0) {
		sp->top = np;
	} else {
		np->next = sp->top;
		sp->top = np;
	}

	sp->length++;
}

/*
 * Pop and return the pointer of the removed top node
 * @param STACK *sp - pointer to the stack
 */
NODE* pop(STACK *sp) {
// your code

	if (sp->length == 0)
		return NULL;

	NODE *node = sp->top;
	sp->top = sp->top->next;
	sp->length--;
	node->next = NULL;

	return node;
}

/*
 * clean the linked list stack
 */
void clean_stack(STACK *sp) {
	clean(&(sp->top));
	sp->top = NULL;
	sp->length = 0;
}
