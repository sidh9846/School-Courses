/*
 -------------------------------------
 File:    queue.c
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
#include "queue.h"

/*
 * Enqueue a node into a queue
 * @param *qp - pointer to the queue
 * @param NODE *np - pointer to the node.
 */
void enqueue(QUEUE *qp, NODE *np) {
// your code

	if (qp->length == 0) {
		qp->front = np;
	} else {
		qp->rear->next = np;
	}

	qp->rear = np;
	qp->length++;
}

/*
 * Dequeue and return the pointer of the removed node.
 * @param *qp - pointer to the queue
 */
NODE* dequeue(QUEUE *qp) {
// your code

	if (qp->length == 0)
		return NULL;

	NODE *node = qp->front;

	qp->front = qp->front->next;
	qp->length--;

	return node;
}

/*
 * Clean the linked list queue
 */
void clean_queue(QUEUE *qp) {
	clean(&(qp->front));
	qp->front = NULL;
	qp->rear = NULL;
	qp->length = 0;
}
