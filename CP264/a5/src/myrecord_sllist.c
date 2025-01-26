/*
 -------------------------------------
 File:    myrecord_sllist.c
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
#include "myrecord_sllist.h"

/**
 * Search singly linked list by the key name.
 *
 * @param SLL *sllp - provides the address of a singly linked list structure.
 * @param char *name - key to search
 * @return Pointer to found node if found; otherwise NULL
 */
NODE* sll_search(SLL *sllp, char *name) {
	NODE *r = NULL;
	NODE *np = sllp->start;
	while (np != NULL) {
		if (strcmp(np->data.name, name) == 0) { // pattern match ??? // action
			return np;
		} else {
			np = np->next;
		}
	}
	return r;
}

/**
 * Insert a new record to linked list at the position sorted by record name field.
 *
 * @param SLL *sllp - provides the address of a singly linked list structure.
 * @param char *name - name field of the new record.
 * @param float score - the score data of the new record.
 */
void sll_insert(SLL *sllp, char *name, float score) {
	// create a node and set data value
	NODE *np = (NODE*) malloc(sizeof(NODE));
	strcpy(np->data.name, name);
	np->data.score = score;
	np->next = NULL;

	// insert the node into the singly linked list
	NODE *prev = NULL;
	NODE *p = sllp->start;
	while (p != NULL && strcmp(name, p->data.name) >= 0) {
		prev = p;
		p = p->next;
	}

	if (prev == NULL) {
		sllp->start = np;
		np->next = p;
	} else {
		prev->next = np;
		np->next = p;
	}

	sllp->length++;
}

/**
 * Delete a node of record matched by the name key from linked list.
 *
 * @param SLL *sllp provides the address of a singly linked list structure.
 * @param name - key used to find the node for deletion.
 * @return 1 if deleted a matched node, 0 otherwise.
 */
int sll_delete(SLL *sllp, char *name) {
	// insert the node into the singly linked list
	NODE *prev = NULL;
	NODE *p = sllp->start;
	while (strcmp(name, p->data.name) != 0) {
		prev = p;
		p = p->next;
	}

	if (p == NULL) {
		return 0;
	} else {
		if (prev == NULL) {
			sllp->start = sllp->start->next;
		} else {
			prev->next = p->next;
		}
		sllp->length--;
		free(p);
		return 1;
	}
}

/**
 * Clean singly linked list, delete all nodes.
 * @param @param SLL *sllp provides the address of a singly linked list structure.
 */
void sll_clean(SLL *sllp) {
	NODE *temp, *ptr = sllp->start;
	while (ptr != NULL) {
		temp = ptr;
		ptr = ptr->next;
		free(temp);
	}
	sllp->start = NULL;
	sllp->length = 0;
}
