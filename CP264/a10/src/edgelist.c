/*
 -------------------------------------
 File:    edgelist.c
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
#include "edgelist.h"

EDGELIST* new_edgelist() {
	EDGELIST *tp = malloc(sizeof(EDGELIST));
	tp->size = 0;
	tp->start = NULL;
	tp->end = NULL;
	return tp;
}

void insert_edge_end(EDGELIST *g, int from, int to, int weight) {
// your code

	EDGENODE *newNode = malloc(sizeof(EDGENODE));

	newNode->from = from;
	newNode->to = to;
	newNode->weight = weight;
	newNode->next = NULL;

	if (g->size == 0) {
		g->start = newNode;
		g->end = newNode;
	} else {
		g->end->next = newNode;
		g->end = newNode;
	}

	g->size++;

}

void insert_edge_start(EDGELIST *g, int from, int to, int weight) {
// your code;

	EDGENODE *newNode = malloc(sizeof(EDGENODE));

	newNode->from = from;
	newNode->to = to;
	newNode->weight = weight;

	if (g->size == 0) {
		g->start = newNode;
		g->end = newNode;
		newNode->next = NULL;
	} else {
		newNode->next = g->start;
		g->start = newNode;
	}

	g->size++;

}

void delete_edge(EDGELIST *g, int from, int to) {
// your code
	EDGENODE *curr = g->start;
	EDGENODE *prev = NULL;

	while (curr != NULL) {
		if (curr->from == from && curr->to == to) {
			if (prev == NULL) {
				g->start = curr->next;
			} else {
				prev->next = curr->next;
			}

			if (curr == g->end) {
				g->end = prev;
			}

			free(curr);
			g->size--;
			return;
		}

		prev = curr;
		curr = curr->next;
	}
}

int weight_edgelist(EDGELIST *g) {
// your code
	EDGENODE *curr = g->start;
	int total = 0;

	while (curr != NULL) {
		total += curr->weight;
		curr = curr->next;
	}

	return total;
}

void clean_edgelist(EDGELIST **gp) {
	EDGELIST *g = *gp;
	EDGENODE *temp, *p = g->start;
	while (p) {
		temp = p;
		p = p->next;
		free(temp);
	}
	free(g);
	*gp = NULL;
}

void display_edgelist(EDGELIST *g) {
	if (g == NULL)
		return;
	printf("size %d ", g->size);
	printf("(from to weight) ");
	EDGENODE *p = g->start;
	while (p) {
		printf("(%d %d %d) ", p->from, p->to, p->weight);
		p = p->next;
	}
}
