/**
 * -------------------------------------
 * @file  queue_linked.c
 * Linked Queue Source Code File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2023-10-08
 *
 * -------------------------------------
 */
// Includes
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "queue_linked.h"

// Functions

// Initializes a queue.
void queue_initialize(queue_linked_struct **queue, data_type_copy copy,
		data_type_string to_string, data_type_destroy destroy) {

	// your code here

	*queue = malloc(sizeof **queue);
	assert((*queue) != NULL);
	(*queue)->front = NULL;
	(*queue)->rear = NULL;
	(*queue)->copy = copy;
	(*queue)->to_string = to_string;
	(*queue)->destroy = destroy;
	return;

}

// Destroys a queue.
void queue_destroy(queue_linked_struct **source) {

	// your code here

	// Free the linked data
	while ((*source)->front != NULL) {
		queue_node *temp = (*source)->front;
		(*source)->destroy(&(temp->item));
		(*source)->front = (*source)->front->next;
		free(temp);
		temp = NULL;
	}
	// Free the queue header
	free(*source);
	*source = NULL;
	return;

}

// Determines if a queue is empty.
bool queue_empty(const queue_linked_struct *source) {

	// your code here

	return (source->front == NULL);

}

// Determines if a queue is full.
bool queue_full(const queue_linked_struct *source) {
	return false;
}

// Returns number of items in queue.
int queue_count(const queue_linked_struct *source) {

	// your code here

	return source->count;

}

// Inserts a copy of an item into a queue.
bool queue_insert(queue_linked_struct *source, const data_type *item) {

	// your code here

	bool inserted = false;
	queue_node *node = malloc(sizeof *node);

	if (node != NULL) {
		node->item = malloc(sizeof *node->item);

		if (node->item != NULL) {
			source->copy(node->item, item);
			source->rear->next = node;
			node->next = NULL;
			source->rear = node;
			inserted = true;
		}
	}
	return inserted;

}

// Returns a copy of the item at the front of a queue, queue is unchanged.
bool queue_peek(const queue_linked_struct *source, data_type *item) {

	// your code here

	bool peeked = false;

	if (source->front != NULL) {
		source->copy(item, source->front->item);
		peeked = true;
	}
	return peeked;

}

// Removes and returns the item at the front of a queue.
bool queue_remove(queue_linked_struct *source, data_type *item) {

	// your code here

	bool removed = false;

	if (source->front != NULL) {
		source->copy(item, source->front->item);
		queue_node *temp = source->front;
		source->front = source->front->next;
		free(temp);
		removed = true;
	}
	return removed;

}

// Prints the items in a queue from front to rear.
void queue_print(const queue_linked_struct *source) {
	char string[DATA_STRING_SIZE];
	queue_node *current = source->front;

	while (current != NULL) {
		printf("%s\n",
				source->to_string(string, DATA_STRING_SIZE, current->item));
		current = current->next;
	}
	return;
}

static void queue_move_front(queue_linked_struct *target,
		queue_linked_struct *source) {
	assert(source->front != NULL);

	queue_node *temp = source->front;
	source->front = source->front->next;
	temp->next = target->front;
	target->front = temp;
	return;
}

// Combines contents of two source queues into a target queue. Items alternate.
void queue_combine(queue_linked_struct *target, queue_linked_struct *source1,
		queue_linked_struct *source2) {

	// your code here

	while (source1->front != NULL && source2->front != NULL) {
		queue_move_front(target, source1);
		queue_move_front(target, source2);
	}
	while (source1->front != NULL) {
		queue_move_front(target, source1);
	}
	while (source2->front != NULL) {
		queue_move_front(target, source2);
	}
	return;

}

// Splits a source queue alternately into two target queues.  Items alternate.
void queue_split_alt(queue_linked_struct *target1, queue_linked_struct *target2,
		queue_linked_struct *source) {

	// your code here

	bool left = true;

	while (source->front != NULL) {

		if (left) {
			queue_move_front(target1, source);
		} else {
			queue_move_front(target2, source);
		}
		left = !left;
	}
	return;

}
