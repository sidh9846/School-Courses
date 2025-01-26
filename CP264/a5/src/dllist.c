/*
 -------------------------------------
 File:    dllist.c
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
#include <string.h>
#include "dllist.h"

/*
 * Create and return a new node using malloc() with passed data value and returns pointer of the node.
 */
NODE* new_node(char value) {
	NODE *node = (NODE*) malloc(sizeof(NODE));

	node->data = value;
	node->prev = NULL;
	node->next = NULL;

	return node;
}

/*
 * Insert a given node at the beginning the of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable
 * @param NODE *np  -  reference of a NODE node to be inserted
 */
void dll_insert_start(DLL *dllp, NODE *np) {
	if (dllp->start == NULL) {
		np->prev = NULL;
		np->next = NULL;
		dllp->start = np;
		dllp->end = np;
	} else {
		np->prev = NULL;
		np->next = dllp->start;
		dllp->start->prev = np;
		dllp->start = np;
	}

	dllp->length++;
}

/*
 * Insert a node at the end of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable
 * @param NODE *np  -  reference of a NODE node to be inserted
 */
void dll_insert_end(DLL *dllp, NODE *np) {
	if (dllp->end == NULL) {
		np->prev = NULL;
		np->next = NULL;
		dllp->start = np;
		dllp->end = np;
	} else {
		np->prev = dllp->end;
		np->next = NULL;
		dllp->end->next = np;
		dllp->end = np;
	}

	dllp->length++;
}

/*
 * This deletes the first node of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable
 */
void dll_delete_start(DLL *dllp) {

	if (dllp->length <= 0)
		return;

	NODE *node = dllp->start;

	if (dllp->length == 1) {
		dllp->start = NULL;
		dllp->end = NULL;
	} else {
		dllp->start = dllp->start->next;
		dllp->start->prev = NULL;
	}

	dllp->length--;
	free(node);
}

/*
 * Delete the end node of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable
 */
void dll_delete_end(DLL *dllp) {

	if (dllp->length <= 0)
		return;

	NODE *node = dllp->end;

	if (dllp->length == 1) {
		dllp->start = NULL;
		dllp->end = NULL;
	} else {
		dllp->end = dllp->end->prev;
		dllp->end->next = NULL;
	}

	dllp->length--;
	free(node);
}

/*
 * Clean and free the nodes of a doubly linked list and reset start and length.
 * @param DLL *dllp -  reference to input DLL variable
 */
void dll_clean(DLL *dllp) {
	NODE *temp, *ptr = dllp->start;
	while (ptr != NULL) {
		temp = ptr;
		ptr = ptr->next;
		free(temp);
	}
	dllp->start = NULL;
	dllp->end = NULL;
	dllp->length = 0;
}
