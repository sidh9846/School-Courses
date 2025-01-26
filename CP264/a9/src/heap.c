/*
 -------------------------------------
 File:    heap.c
 Project: a9
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-03-19
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "heap.h"

int cmp(KEYTYPE a, KEYTYPE b) {
	int r = 0;
	if (a < b)
		r = -1;
	else if (a > b)
		r = 1;
	return r;
}

HEAP* new_heap(int capacity) {
	HEAP *hp = (HEAP*) malloc(sizeof(HEAP));
	if (hp == NULL)
		return NULL;
	hp->hda = (HEAPDATA*) malloc(sizeof(HEAPDATA) * capacity);
	if (hp->hda == NULL) {
		free(hp);
		return NULL;
	};
	hp->capacity = capacity;
	hp->size = 0;
	return hp;
}

// you may add this function to be used other functions.
int heapify_up(HEAPDATA *hda, int index) {
// your code
	int parent = (index - 1) / 2;
	while (index > 0 && cmp(hda[index].key, hda[parent].key) < 0) {
		HEAPDATA temp = hda[index];
		hda[index] = hda[parent];
		hda[parent] = temp;

		index = parent;
		parent = (index - 1) / 2;
	}
	return index;

}

// you may add this function to be used other functions.
int heapify_down(HEAPDATA *hda, int n, int index) {
// your code
	int left, right, min;
	while (index < n) {
		left = 2 * index + 1;
		right = 2 * index + 2;
		min = index;

		if (left < n && cmp(hda[left].key, hda[min].key) < 0)
			min = left;

		if (right < n && cmp(hda[right].key, hda[min].key) < 0)
			min = right;

		if (min == index)
			break;

		HEAPDATA temp = hda[index];
		hda[index] = hda[min];
		hda[min] = temp;
		index = min;
	}
	return index;
}

void heap_insert(HEAP *heap, HEAPDATA new_node) {
// your code
	if (heap->size >= heap->capacity) {
		heap->capacity *= 2;
		heap->hda = realloc(heap->hda, sizeof(HEAPDATA) * heap->capacity);
	}

	int index = heap->size;
	heap->hda[index] = new_node;
	heap->size++;

	heapify_up(heap->hda, index);
}

HEAPDATA heap_find_min(HEAP *heap) {
// your code
	if (heap->size == 0) {
		exit(EXIT_FAILURE);
	}
	return heap->hda[0];
}

HEAPDATA heap_extract_min(HEAP *heap) {
// your code

	if (heap->size == 0) {
		exit(EXIT_FAILURE);
	}

	HEAPDATA min = heap->hda[0];

	heap->hda[0] = heap->hda[heap->size - 1];
	heap->size--;

	heapify_down(heap->hda, heap->size, 0);

	return min;

}

int heap_change_key(HEAP *heap, int index, KEYTYPE new_key) {
// your code
	if (index < 0 || index >= heap->size) {
		exit(EXIT_FAILURE);
	}

	KEYTYPE old_key = heap->hda[index].key;
	heap->hda[index].key = new_key;

	if (cmp(new_key, old_key) < 0)
		return heapify_up(heap->hda, index);
	else if (cmp(new_key, old_key) > 0)
		return heapify_down(heap->hda, heap->size, index);
	else
		return index;
}

int heap_search_data(HEAP *heap, VALUETYPE data) {
// your code
	for (int i = 0; i < heap->size; i++) {
		if (heap->hda[i].value == data)
			return i;
	}
	return -1;
}

void heap_clean(HEAP **heapp) {
	if (heapp) {
		HEAP *heap = *heapp;
		if (heap->capacity > 0) {
			heap->capacity = 0;
			heap->size = 0;
			free(heap->hda);
			free(heap);
		}
		*heapp = NULL;
	}
}
