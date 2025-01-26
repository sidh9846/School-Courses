/**
 * -------------------------------------
 * @file  graph_am.c
 * Adjacency Matrix Graph Code File
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-03-14
 *
 * -------------------------------------
 */
#include "graph_am.h"
#include <stdbool.h> // For boolean type
#include <limits.h> // For INT_MAX

// Initializes an adjacency matrix graph.
graph_am* graph_am_initialize(int size) {
	graph_am *source = malloc(sizeof *source);
	source->size = size;
	// Initialize values to zeroes.
	source->values = calloc(size * size, sizeof *source->values);
	return source;
}

void graph_am_free(graph_am **source) {
	// Free up the data array.
	free((*source)->values);
	(*source)->values = NULL;
	free(*source);
	*source = NULL;
	return;
}

int graph_am_add_vertice(graph_am *source, const graph_am_pair *pair) {
	int added = 0;

	// your code here

	if (pair->row >= 0 && pair->col >= 0 && pair->row <= source->size
			&& pair->col <= source->size) {

		if (*(source->values + pair->row * source->size + pair->col) > 0)
			return added;

		if (pair->row == pair->col) {
			*(source->values + pair->row * source->size + pair->col) = 2;
		} else {
			*(source->values + pair->row * source->size + pair->col) = 1;
			*(source->values + pair->col * source->size + pair->row) = 1;
		}

		added = 1;

	}

	return added;
}

int graph_am_remove_vertice(graph_am *source, const graph_am_pair *pair) {
	int removed = 0;

	// your code here

	if (pair->row >= 0 && pair->col >= 0 && pair->row <= source->size
			&& pair->col <= source->size) {

		if (*(source->values + pair->row * source->size + pair->col) == 0)
			return removed;

		*(source->values + pair->row * source->size + pair->col) = 0;
		*(source->values + pair->col * source->size + pair->row) = 0;

		removed = 1;

	}

	return removed;
}

graph_am* graph_am_create(int size, const graph_am_pair pairs[], int count) {
	graph_am *source = graph_am_initialize(size);

	// your code here

	for (int i = 0; i < count; i++) {
		graph_am_add_vertice(source, &pairs[i]);
	}

	return source;
}

void graph_am_neighbours(const graph_am *source, int vertex, int vertices[],
		int *count) {

	// your code here

	if (vertex < 0 || vertex >= source->size)
		return;

	*count = 0;

	for (int i = 0; i < source->size; i++) {
		if (*(source->values + i * source->size + vertex) > 0) {
			vertices[*count] = i;
			(*count)++;
		}
	}

	return;
}

int graph_am_degree(const graph_am *source, int vertex) {
	int connected = 0;

// your code here

	if (vertex < 0 || vertex >= source->size)
		return connected;

	for (int i = 0; i < source->size; i++) {
		if (*(source->values + i * source->size + vertex) == 1) {
			connected++;
		} else if (*(source->values + i * source->size + vertex) == 2) {
			connected += 2;
		}
	}

	return connected;
}

static void graph_am_breadth_traversal_aux(const graph_am *source, int *visited,
		int *queue, int *front, int *rear, int vertices[], int *count) {
	// empty
	if (*front > *rear)
		return;

	// Dequeue a vertex
	int curr = queue[(*front)++];
	vertices[(*count)++] = curr;

	// Visit all
	for (int i = 0; i < source->size; i++) {
		// if the vertex is adjacent and not visited
		if (*(source->values + curr * source->size + i) > 0
				&& visited[i] == 0) {
			// vertex visited
			visited[i] = 1;
			// Enqueue
			queue[++(*rear)] = i;
		}
	}

	// traverse
	graph_am_breadth_traversal_aux(source, visited, queue, front, rear,
			vertices, count);
}

// Performs a breadth-first traversal of a graph recursively
void graph_am_breadth_traversal(const graph_am *source, int vertex,
		int vertices[], int *count) {

	// invalid inputs
	if (source == NULL || vertices == NULL || count == NULL || vertex < 0
			|| vertex >= source->size)
		return;

	// Initialize array
	int visited[source->size];
	for (int i = 0; i < source->size; i++)
		visited[i] = 0;

	// Initialize queue
	int queue[source->size];
	int front = 0; // Front of the queue
	int rear = -1; // Rear of the queue (initialized to -1 for empty queue)

	// Enqueue
	queue[++rear] = vertex;
	visited[vertex] = 1;

	// Initialize count
	*count = 0;

	// traverse recursively
	graph_am_breadth_traversal_aux(source, visited, queue, &front, &rear,
			vertices, count);
}

static void graph_am_depth_traversal_aux(const graph_am *source, int vertex,
		int *visited, int stack[], int *top, int vertices[], int *count) {

	// current vertex visited
	visited[vertex] = 1;
	vertices[(*count)++] = vertex;

	// Visit all
	for (int i = 0; i < source->size; i++) {
		if (*(source->values + vertex * source->size + i) > 0
				&& visited[i] == 0) {
			// Push
			stack[++(*top)] = i;
			// visit the adjacent
			graph_am_depth_traversal_aux(source, i, visited, stack, top,
					vertices, count);
		}
	}
}

// Performs a depth-first traversal of a graph recursively
void graph_am_depth_traversal(const graph_am *source, int vertex,
		int vertices[], int *count) {

	// invalid inputs
	if (source == NULL || vertices == NULL || count == NULL || vertex < 0
			|| vertex >= source->size)
		return;

	// Initialize visited vertices array
	int visited[source->size];
	for (int i = 0; i < source->size; i++)
		visited[i] = 0;

	// Initialize stack
	int stack[source->size];
	int top = -1;

	// Initialize count
	*count = 0;

	// traverse recursively
	graph_am_depth_traversal_aux(source, vertex, visited, stack, &top, vertices,
			count);
}

// Prints the contents of an adjacency matrix graph.
void graph_am_print(const graph_am *source) {
// Print the column numbers.
	printf("    ");

	for (int i = 0; i < source->size; i++)
		printf("%3d", i);
	printf("\n");
	printf("    ");
	for (int i = 0; i < source->size; i++)
		printf("---");
	printf("\n");

// Print the row numbers and rows.
	for (int i = 0; i < source->size; i++) {
		printf("%3d|", i);

		for (int j = 0; j < source->size; j++) {
			// find item using offsets
			printf("%3d", *(source->values + i * source->size + j));
		}
		printf("\n");
	}
}
