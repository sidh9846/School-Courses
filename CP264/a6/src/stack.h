/*
 -------------------------------------
 File:    stack.h
 Project: a6
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-20
 -------------------------------------
 */
#ifndef STACK_H_
#define STACK_H_
#include "common.h"

/*
 * Define a structure STACK containing the length and pointer of the top node.
 * int length - maintains the length of stack.
 * NODE *top - pointer to the top node of linked list stack
 */
typedef struct stack {
	int length;
	NODE *top;
} STACK;

/*
 * Push a node into a linked list stack
 * @param STACK *sp - pointer to the stack
 * @param NODE *np - pointer to the node.
 */
void push(STACK *sp, NODE *np);

/*
 * Pop and return the pointer of the removed top node
 * @param STACK *sp - pointer to the stack
 */
NODE* pop(STACK *sp);

/*
 * clean the linked list stack
 */
void clean_stack(STACK *sp);

#endif /* STACK_H_ */
