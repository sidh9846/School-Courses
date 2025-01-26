/**
 * -------------------------------------
 * @file  name_set_initialize.c
 * Lab 5 Source Code File
 * -------------------------------------
 * @author Heider Ali, 999999999, heali@wlu.ca
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2024-02-09
 *
 * -------------------------------------
 */
#include "name_set.h"

name_set* name_set_initialize() {
	// Allocate memory to the data structure
	name_set *set = malloc(sizeof *set);
	// Initialize the header fields.
	set->front = NULL;
	set->rear = NULL;
	return set;
}

int name_set_free(name_set **set) {

	// your code here
	int freed;

	name_set_node *curr = (*set)->front;
	name_set_node *next;

	while (curr != NULL) {
		next = curr->next;
		free(curr);
		freed++;
		curr = next;
	}

	free(*set);
	*set = NULL;

	return freed;

}

BOOLEAN name_set_append(name_set *set, const char *first_name,
		const char *last_name) {

// your code here
	if (name_set_contains(set, first_name, last_name)) {
		return FALSE;
	}

	name_set_node *newNode = malloc(sizeof(name_set_node));

	strcpy(newNode->first_name, first_name);
	strcpy(newNode->last_name, last_name);
	newNode->next = NULL;

	if (set->front == NULL) {
		set->front = newNode;
		set->rear = newNode;
	} else {
		set->rear->next = newNode;
		set->rear = newNode;
	}

	return TRUE;

}

BOOLEAN name_set_contains(const name_set *set, const char *first_name,
		const char *last_name) {

// your code here

	name_set_node *curr = set->front;

	while (curr != NULL) {
		if (strcmp(curr->first_name, first_name) == 0
				&& strcmp(curr->last_name, last_name) == 0) {
			return TRUE;
		}
		curr = curr->next;
	}

	return FALSE;
}

void name_set_print(const name_set *set) {

// your code here

	name_set_node *curr = set->front;

	while (curr != NULL) {
		printf("%s, %s\n", curr->first_name, curr->last_name);
		curr = curr->next;
	}

}
