/**
 * -------------------------------------
 * @file  queue_linked.h
 * Linked Queue Header File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2023-10-08
 *
 * -------------------------------------
 * DO NOT CHANGE CONTENTS
 */
#ifndef QUEUE_LINKED_H_
#define QUEUE_LINKED_H_

// Includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>
#include <assert.h>

#include "data.h"

/**
 * Queue node.
 */
typedef struct queue_node {
	data_type *item;          // Pointer to the node data_type .
	struct queue_node *next; // Pointer to the next queue node.
} queue_node;

/**
 * Queue header.
 */
typedef struct {
	queue_node *front;          // Pointer to the front node of the queue.
	queue_node *rear;           // Pointer to the rear node of the queue.
	int count;                  // Number of items in queue.
	data_type_copy copy;        // Pointer to data_type  copy function.
	data_type_string to_string; // Pointer to data_type  to string function.
	data_type_destroy destroy;  // Pointer to data_type  destroy function.
} queue_linked_struct;

// Prototypes

/**
 * Initializes a queue.
 *
 * @param queue - pointer to the queue to initialize.
 * @param copy - the data copy function
 * @param to_string - the data to_string function
 * @param destroy - the data destroy function
 */
void queue_initialize(queue_linked_struct **queue, data_type_copy copy,
		data_type_string to_string, data_type_destroy destroy);

/**
 * Destroys a queue.
 *
 * @param source - pointer to a queue
 */
void queue_destroy(queue_linked_struct **source);

/**
 * Determines if a queue is empty.
 *
 * @param source - pointer to a queue.
 * @return - true if source is empty, false otherwise.
 */
bool queue_empty(const queue_linked_struct *source);

/**
 * Determines if a queue is full.
 *
 * @param source - pointer to a queue.
 * @return - true if the queue is full, false otherwise.
 */
bool queue_full(const queue_linked_struct *source);

/**
 * Returns number of items in queue.
 *
 * @param source - pointer to a queue.
 * @return - number of items in queue.
 */
int queue_count(const queue_linked_struct *source);

/**
 * Inserts a copy of an item into a queue.
 *
 * @param source - pointer to a queue
 * @param item - pointer to the item to push
 * @return - true if item inserted, false otherwise
 */
bool queue_insert(queue_linked_struct *source, const data_type *item);

/**
 * Returns a copy of the item at the front of a queue, queue is unchanged.
 *
 * @param source - pointer to a queue
 * @param item - pointer to a copy of the item to retrieve
 * @return - true if item peeked, false otherwise (queue is empty)
 */
bool queue_peek(const queue_linked_struct *source, data_type *item);

/**
 * Removes and returns the item at the front of a queue.
 *
 * @param queue - pointer to a queue
 * @param item - pointer to the item to remove
 * @return - true if item popped, false otherwise (queue is empty)
 */
bool queue_remove(queue_linked_struct *source, data_type *item);

/**
 * Prints the items in a queue from front to rear.
 * (For testing only).
 *
 * @param queue - pointer to a queue
 */
void queue_print(const queue_linked_struct *source);

/**
 * Moves the front node of a queue stack to a target queue.
 *
 * @param target - pointer to target queue
 * @param source - pointer to source queue
 */
static void queue_move_front(queue_linked_struct *target,
		queue_linked_struct *source);

/**
 * Combines contents of two source queues into a target queue. Items alternate.
 * Source queues are empty (not destroyed) when the function completes.
 * Moves nodes, not data.
 *
 * @param target - pointer to target queue
 * @param source1 - pointer to first source queue
 * @param source2 - pointer to second source queue
 */
void queue_combine(queue_linked_struct *target, queue_linked_struct *source1,
		queue_linked_struct *source2);

/**
 * Splits a source queue alternately into two target queues.  Items alternate.
 * Source queue is empty (not destroyed) when function completes.
 * Moves nodes, not data.
 *
 * @param target1 - pointer to first target queue
 * @param target2 - pointer to second target queue
 * @param source - pointer to source queue
 */
void queue_split_alt(queue_linked_struct *target1, queue_linked_struct *target2,
		queue_linked_struct *source);

#endif /* QUEUE_LINKED_H_ */
