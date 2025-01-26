/*
 -------------------------------------
 File:    myrecord_bst.c
 Project: a7
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-03-08
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "queue_stack.h"
#include "bst.h"
#include "myrecord_bst.h"

// Helper function to traverse the BST in order and store data in an array
static void bst_traverse_inorder(BSTNODE *root, float *data, int *index) {
	if (root == NULL) {
		return;
	}
	bst_traverse_inorder(root->left, data, index);
	data[(*index)++] = root->data.score;
	bst_traverse_inorder(root->right, data, index);
}

// Helper function to compute the standard deviation of the data
static float compute_stddev(float mean, float *data, int count) {
	float sum = 0.0f;
	for (int i = 0; i < count; i++) {
		sum += powf(data[i] - mean, 2.0f);
	}
	return sqrtf(sum / count);
}

// Add a record to the BSTDS and update its statistics
void add_record(BSTDS *tree, RECORD record) {
	// Insert the record into the BST
	bst_insert(&(tree->root), record);

	// Update count
	tree->count++;

	// Update mean
	tree->mean = (tree->mean * (tree->count - 1) + record.score) / tree->count;

	// Update standard deviation and median
	if (tree->count == 1) {
		tree->stddev = 0;
	} else {
		// Allocate memory for storing data
		float *data = (float*) malloc(tree->count * sizeof(float));

		// Traverse the BST in order and store data in the array
		int index = 0;
		bst_traverse_inorder(tree->root, data, &index);

		// Compute the new standard deviation
		tree->stddev = compute_stddev(tree->mean, data, tree->count);

		// Free the allocated memory
		free(data);
	}
}

// Remove a record from the BSTDS and update its statistics
void remove_record(BSTDS *tree, char *key) {
	BSTNODE **root = &(tree->root);
	float score = (bst_search(tree->root, key))->data.score;
	float mean = tree->mean;

	bst_delete(root, key);

	tree->count--;

	if (tree->count == 0) {
		tree->mean = 0;
	} else {
		tree->mean = mean - (score - mean) / tree->count;
	}

	if (tree->count < 2) {
		tree->stddev = 0;
	} else {
		tree->stddev = sqrt(
				(((tree->count + 1) * (pow(tree->stddev, 2) + pow(mean, 2)))
						- pow(score, 2)) / tree->count - pow(tree->mean, 2));
	}
}

// Clean up the BSTDS
void clean_bstds(BSTDS *ds) {
	clean_bst(&(ds->root));
	ds->count = 0;
	ds->mean = 0;
	ds->stddev = 0;
}
