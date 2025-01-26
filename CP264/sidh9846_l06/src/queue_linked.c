/**
 * -------------------------------------
 * @file  queue_linked.c
 * Linked Queue Source Code File
 * -------------------------------------
 * @author * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-02-22
 *
 * -------------------------------------
 */
// Includes
#include "queue_linked.h"

// Functions

queue_linked* queue_initialize() {

	// your code here

	// Allocate memory to the queue header
	queue_linked *source = malloc(sizeof *source);
	// Initialize the stack top
	source->front = NULL;
	return source;

}

void queue_free(queue_linked **source) {

	// your code here

	// Free the linked data
	while ((*source)->front != NULL) {
		queue_node *temp = (*source)->front;
		// use the data_free function to free the actual data
		data_free(&temp->item);
		// update the queue front
		(*source)->front = (*source)->front->next;
		// free the stack node
		free(temp);
		temp = NULL;
	}
	// Free the queue header
	free(*source);
	*source = NULL;
	return;

}

BOOLEAN queue_empty(const queue_linked *source) {

	// your code here

	return (source->front == NULL);

}

int queue_count(const queue_linked *source) {

	// your code here

	return source->count;

}

void queue_insert(queue_linked *source, data_ptr item) {

	// your code here

	// allocate memory to a new queue node
	queue_node *node = malloc(sizeof *node);
	// allocate memoory for the data
	node->item = malloc(sizeof *node->item);
	// copy the data parameter to the new memory
	data_copy(node->item, item);
	// update the queue rear
	node->next = NULL;
	printf("here");
	if (source->count == 0) {
		source->front = node;
	} else {
		source->rear->next = node;
	}
	source->rear = node;
	source->count++;

}

BOOLEAN queue_peek(const queue_linked *source, data_ptr item) {

	// your code here

	BOOLEAN peeked = FALSE;

	if (source->front != NULL) {
		// return a copy of the data in the node
		data_copy(item, source->front->item);
		peeked = TRUE;
	}
	return peeked;

}

BOOLEAN queue_remove(queue_linked *source, data_ptr *item) {

	// your code here

	BOOLEAN popped = FALSE;

	if (source->front != NULL) {
		// return a pointer to the node data
		*item = source->front->item;
		queue_node *temp = source->front;
		// update the stack top and free the removed node
		source->front = source->front->next;
		free(temp);
		popped = TRUE;
		source->count--;
	}

	if (source->count == 0) {
		source->front = NULL;
		source->rear = NULL;
	}

	return popped;

}

void queue_print(const queue_linked *source) {
	char string[DATA_STRING_SIZE];
	queue_node *current = source->front;

	while (current != NULL) {
		printf("%s\n", data_string(string, sizeof string, current->item));
		current = current->next;
	}
	return;
}
