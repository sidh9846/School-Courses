/*
 -------------------------------------
 File:    graph.c
 Project: a10
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-04-02
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "queue_stack.h"
#include "graph.h"
#include <limits.h>

#define INFINITY INT_MAX // Assuming you have defined INFINITY elsewhere

GRAPH* new_graph(int order) {
	GRAPH *gp = malloc(sizeof(GRAPH));
	gp->nodes = malloc(order * sizeof(GNODE*));

	int i;
	for (i = 0; i < order; i++) {
		gp->nodes[i] = malloc(sizeof(GNODE));
		gp->nodes[i]->nid = i;
		strcpy(gp->nodes[i]->name, "null");
		gp->nodes[i]->neighbor = NULL;
	}

	gp->order = order;
	gp->size = 0;

	return gp;
}

void insert_edge_graph(GRAPH *g, int from, int to, int weight) {
// your code

// Check if the edge already exists
	ADJNODE *ptr = g->nodes[from]->neighbor;
	while (ptr != NULL) {
		if (ptr->nid == to) {
			// Edge already exists, update its weight
			ptr->weight = weight;
			return;
		}
		ptr = ptr->next;
	}

	// Edge doesn't exist, create a new edge
	ADJNODE *new_edge = (ADJNODE*) malloc(sizeof(ADJNODE));
	if (new_edge == NULL)
		return; // Memory allocation failed

	new_edge->nid = to;
	new_edge->weight = weight;
	new_edge->next = NULL;

	// Insert the new edge at the end of the neighbor list for the 'from' node
	if (g->nodes[from]->neighbor == NULL) {
		// If 'from' node has no neighbors yet
		g->nodes[from]->neighbor = new_edge;
	} else {
		// Traverse to the end of the neighbor list
		ptr = g->nodes[from]->neighbor;
		while (ptr->next != NULL) {
			ptr = ptr->next;
		}
		// Insert the new edge
		ptr->next = new_edge;
	}

	// Increment the number of edges in the graph
	g->size++;
}

void delete_edge_graph(GRAPH *g, int from, int to) {
// your code

	ADJNODE *prev = NULL;
	ADJNODE *curr = g->nodes[from]->neighbor;

	// Traverse the adjacency list of the 'from' node to find the edge to be deleted
	while (curr != NULL) {
		if (curr->nid == to) {
			// Found the edge to be deleted
			if (prev == NULL) {
				// If the edge is the first in the list
				g->nodes[from]->neighbor = curr->next;
			} else {
				prev->next = curr->next;
			}
			// Free the memory allocated for the edge
			free(curr);
			// Decrement the number of edges in the graph
			g->size--;
			return;
		}
		// Move to the next edge in the list
		prev = curr;
		curr = curr->next;
	}
}

int get_edge_weight(GRAPH *g, int from, int to) {
// your code
	ADJNODE *ptr = g->nodes[from]->neighbor;

	// Traverse the adjacency list of the 'from' node to find the edge
	while (ptr != NULL) {
		if (ptr->nid == to) {
			// Found the edge, return its weight
			return ptr->weight;
		}
		// Move to the next edge in the list
		ptr = ptr->next;
	}

	// Edge not found, return INFINITY (or any sentinel value indicating absence of edge)
	return INFINITY;
}

void traverse_bforder(GRAPH *g, int nid) {
// your code
	if (g == NULL || nid < 0 || nid >= g->order)
		return;

	// Create a queue for BFS traversal
	QUEUE *q = malloc(sizeof(QUEUE));
	if (q == NULL)
		return;
	q->front = NULL;
	q->rear = NULL;

	// Array to keep track of visited nodes
	int *visited = (int*) calloc(g->order, sizeof(int));
	if (visited == NULL) {
		free(q);
		return;
	}

	// Enqueue the starting node
	enqueue(q, &g->nodes[nid]);

	// Mark the starting node as visited
	visited[nid] = 1;

	// Traverse the graph in BFS order
	while (q->front != NULL) {
		GNODE *node = *(GNODE**) dequeue(q);
		printf("(%d %s) ", node->nid, node->name);

		// Traverse all neighbors of the current node
		ADJNODE *neighbor = node->neighbor;
		while (neighbor != NULL) {
			int neighbor_id = neighbor->nid;
			if (!visited[neighbor_id]) {
				// If neighbor not visited, enqueue it and mark as visited
				enqueue(q, &g->nodes[neighbor_id]);
				visited[neighbor_id] = 1;
			}
			neighbor = neighbor->next;
		}
	}

	// Free memory used by the queue and visited array
	clean_queue(q);
	free(visited);
}

// Use auxiliary stack data structure for the algorithm
void traverse_dforder(GRAPH *g, int nid) {
// your code
	if (g == NULL || nid < 0 || nid >= g->order)
		return;

	// Create a stack for DFS traversal
	STACK *s = malloc(sizeof(STACK));
	if (s == NULL)
		return;
	s->top = NULL;

	// Array to keep track of visited nodes
	int *visited = (int*) calloc(g->order, sizeof(int));
	if (visited == NULL) {
		free(s);
		return;
	}

	// Push the starting node onto the stack
	push(s, &g->nodes[nid]);

	// Mark the starting node as visited
	visited[nid] = 1;

	// Traverse the graph in DFS order
	while (s->top != NULL) {
		GNODE *node = *(GNODE**) pop(s);
		printf("(%d %s) ", node->nid, node->name);

		// Traverse all neighbors of the current node
		ADJNODE *neighbor = node->neighbor;
		while (neighbor != NULL) {
			int neighbor_id = neighbor->nid;
			if (!visited[neighbor_id]) {
				// If neighbor not visited, push it onto the stack and mark as visited
				push(s, &g->nodes[neighbor_id]);
				visited[neighbor_id] = 1;
			}
			neighbor = neighbor->next;
		}
	}

	// Free memory used by the stack and visited array
	clean_stack(s);
	free(visited);
}

void clean_graph(GRAPH **gp) {
	int i;
	GRAPH *g = *gp;
	ADJNODE *temp, *ptr;
	for (i = 0; i < g->order; i++) {
		ptr = g->nodes[i]->neighbor;
		while (ptr != NULL) {
			temp = ptr;
			ptr = ptr->next;
			free(temp);
		}
		free(g->nodes[i]);
	}
	free(g->nodes);
	free(g);
	*gp = NULL;
}

void display_graph(GRAPH *g) {
	if (g) {
		printf("order %d ", g->order);
		printf("size %d ", g->size);
		printf("(from to weight) ");
		int i;
		ADJNODE *ptr;
		for (i = 0; i < g->order; i++) {
			//printf("\n%d:", g->nodes[i]->nid);
			ptr = g->nodes[i]->neighbor;
			while (ptr != NULL) {
				printf("(%d %d %d) ", i, ptr->nid, ptr->weight);
				ptr = ptr->next;
			}
		}
	}
}
