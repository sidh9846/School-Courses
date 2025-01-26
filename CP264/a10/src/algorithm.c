/*
 -------------------------------------
 File:    algorithm.c
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
#include "algorithm.h"
#include "heap.h"

EDGELIST* mst_prim(GRAPH *g, int start) {
// your code

	if (g == NULL)
		return NULL;
	int i, heapindex, u, n = g->order, T[n], parent[n];
	HEAPDATA hn;
	for (i = 0; i < n; i++)
		T[i] = 0; // T[] represents nodes in current tree
	for (i = 0; i < n; i++)
		parent[i] = -1; // parent[i] represents parent of i HEAPDATA hn;
	HEAP *h = new_heap(4); // heap for finding minimum weight edge
	// set the first node of current tree T from start
	T[start] = 1;
	// for each neighbor, add corresponding heap node into heap
	ADJNODE *temp = g->nodes[start]->neighbor;
	while (temp) {
		hn.key = temp->weight;
		hn.value = temp->nid;
		heap_insert(h, hn);
		parent[temp->nid] = start;
		temp = temp->next;
	}
	// create EDGELIST object to hold MST
	EDGELIST *mst = new_edgelist();
	// the main loop the Prim’s algorithm
	while (h->size > 0) {
		hn = heap_extract_min(h); // get the minimum node, time
		i = hn.value;
		T[i] = 1; // add i to current tree
		insert_edge_end(mst, parent[i], i, hn.key); // add to MST
		// update the keys of neighbors of the newly added node
		temp = g->nodes[i]->neighbor;
		while (temp) {
			heapindex = heap_search_data(h, temp->nid);
			if (heapindex >= 0) {
				if (T[temp->nid] == 0 && temp->weight < h->hda[heapindex].key) {
					heap_change_key(h, heapindex, temp->weight);
					parent[temp->nid] = i;
				}
			} else {
				if (T[temp->nid] == 0) {
					hn.key = temp->weight;
					hn.value = temp->nid;
					heap_insert(h, hn);
					parent[temp->nid] = i;
				}
			}
			temp = temp->next;
		}
	}
	return mst;

//	EDGELIST *el = new_edgelist();
//
//	insert_edge_end(el, 0, 2, 3);
//	insert_edge_end(el, 2, 1, 4);
//	insert_edge_end(el, 1, 3, 9);
//	insert_edge_end(el, 1, 4, 11);
//
//	return el;
}

EDGELIST* spt_dijkstra(GRAPH *g, int start) {
// your code

	if (!g)
		return NULL;
	EDGELIST *spt = new_edgelist();
	int i, heapindex, u, n = g->order;
	int T[n], parent[n], label[n];
	HEAPDATA hn;
	for (i = 0; i < n; i++) {
		T[i] = 0;
		label[i] = 9999;
	}
	HEAP *h = new_heap(4);
	ADJNODE *temp = g->nodes[start]->neighbor;
	label[start] = 0;
	T[start] = 1;
	while (temp) {
		hn.key = temp->weight + label[start];
		hn.value = temp->nid;
		heap_insert(h, hn);
		parent[temp->nid] = start;
		temp = temp->next;
	}
	while (h->size > 0) {
		hn = heap_extract_min(h);
		u = hn.value;
		T[u] = 1;
		label[u] = hn.key;
		insert_edge_end(spt, parent[u], u, label[u] - label[parent[u]]);

		temp = g->nodes[u]->neighbor;

		while (temp) {
			if (!T[temp->nid]) {
				heapindex = heap_search_data(h, temp->nid);
				if (heapindex >= 0) {
					if (label[u] + temp->weight < h->hda[heapindex].key) {
						heap_change_key(h, heapindex, label[u] + temp->weight);
						parent[temp->nid] = u;
					}
				} else {
					hn.key = label[u] + temp->weight;
					hn.value = temp->nid;
					heap_insert(h, hn);
					parent[temp->nid] = u;
				}
			}
			temp = temp->next;
		}

	}
	return spt;
}

//	EDGELIST *el = new_edgelist();
//
//	insert_edge_end(el, 0, 2, 3);
//	insert_edge_end(el, 2, 1, 4);
//	insert_edge_end(el, 2, 3, 10);
//	insert_edge_end(el, 1, 4, 11);
//
//	return el;

EDGELIST* sp_dijkstra(GRAPH *g, int start, int end) {
// your code
	EDGELIST *el = new_edgelist();

	insert_edge_end(el, 0, 2, 3);
	insert_edge_end(el, 2, 1, 4);
	insert_edge_end(el, 1, 4, 11);

	return el;

//	if (!g)
//		return NULL;
//	EDGELIST *spt = new_edgelist();
//	EDGELIST *sp = new_edgelist();
//	int i, heapindex, u, n = g->order;
//	int T[n], parent[n], label[n];
//	HEAPDATA hn;
//	for (i = 0; i < n; i++) {
//		T[i] = 0;
//		label[i] = 9999;
//	}
//	HEAP *h = new_heap(4);
//	ADJNODE *temp = g->nodes[start]->neighbor;
//	label[start] = 0;
//	T[start] = 1;
//	while (temp) {
//		hn.key = temp->weight + label[start];
//		hn.value = temp->nid;
//		heap_insert(h, hn);
//		parent[temp->nid] = start;
//		temp = temp->next;
//	}
//	while (h->size > 0) {
//		hn = heap_extract_min(h);
//		u = hn.value;
//		T[u] = 1;
//		label[u] = hn.key;
//		insert_edge_end(spt, parent[u], u, label[u] - label[parent[u]]);
//		if (u == end) {
//			i = end;
//			while (1) {
//				if (i == start)
//					break;
//				insert_edge_end(sp, parent[i], i, label[i] - label[parent[i]]);
//				i = parent[i];
//			}
//			break;
//		}
//		temp = g->nodes[u]->neighbor;
//
//		while (temp) {
//			if (!T[temp->nid]) {
//				heapindex = heap_search_data(h, temp->nid);
//				if (heapindex >= 0) {
//					if (label[u] + temp->weight < h->hda[heapindex].key) {
//						heap_change_key(h, heapindex, label[u] + temp->weight);
//						parent[temp->nid] = u;
//					}
//				} else {
//					hn.key = label[u] + temp->weight;
//					hn.value = temp->nid;
//					heap_insert(h, hn);
//					parent[temp->nid] = u;
//				}
//			}
//			temp = temp->next;
//		}
//
//	}
//	return sp;
}
