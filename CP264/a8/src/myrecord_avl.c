/*
 -------------------------------------
 File:    myrecord_avl.c
 Project: a8
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-03-13
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "avl.h"
#include "myrecord_avl.h"

void merge_avl(AVLNODE **dest_rootp, AVLNODE **source_rootp) {
	if (*source_rootp == NULL) {
		return;
	}
	if (*dest_rootp == NULL) {
		*dest_rootp = *source_rootp;
		*source_rootp = NULL;
		return;
	}
	AVLNODE *source_root = *source_rootp;
	merge_avl(dest_rootp, &source_root->left);
	merge_avl(dest_rootp, &source_root->right);
	avl_insert(dest_rootp, source_root->data);
	free(source_root);
}

void merge_avlds(AVLDS *dest, AVLDS *source) {
	merge_avl(&(dest->root), &(source->root));
	dest->count += source->count;
	dest->mean = (dest->mean * dest->count + source->mean * source->count)
			/ (dest->count + source->count);
	dest->stddev = sqrt(
			((dest->stddev * dest->stddev + dest->mean * dest->mean)
					* dest->count
					+ (source->stddev * source->stddev
							+ source->mean * source->mean) * source->count)
					/ (dest->count + source->count) - dest->mean * dest->mean);
	source->root = NULL;
	source->count = 0;
	source->mean = 0;
	source->stddev = 0;
}

void clean_avlds(AVLDS *ds) {
	clean_avl(&ds->root);
	ds->count = 0;
	ds->mean = 0;
	ds->stddev = 0;
}

// the following functions are adapted from a7q3
void add_record(AVLDS *tree, RECORD data) {
	if (avl_search(tree->root, data.name) == NULL) {
		avl_insert(&(tree->root), data);
		int count = tree->count;
		float mean = tree->mean;
		float stddev = tree->stddev;
		tree->count = count + 1;
		tree->mean = (mean * count + data.score) / (count + 1.0);
		tree->stddev = sqrt(
				data.score * data.score / (count + 1.0)
						+ (stddev * stddev + mean * mean)
								* (count / (count + 1.0))
						- tree->mean * tree->mean);
	} else {
		printf("record exits");
	}
}

void remove_record(AVLDS *tree, char *name) {
	AVLNODE *np = NULL;
	if ((np = avl_search(tree->root, name)) != NULL) {
		float score = np->data.score;
		avl_delete(&(tree->root), name);
		float count = tree->count;
		float mean = tree->mean;
		float stddev = tree->stddev;
		tree->count = count - 1;
		if (count >= 3) {
			tree->mean = (mean * count - score) / (count - 1.0);
			tree->stddev = sqrt(
					(stddev * stddev + mean * mean) * (count / (count - 1.0))
							- score * score / (count - 1.0)
							- tree->mean * tree->mean);
		} else if (count == 2) {
			tree->mean = mean * count - score;
			tree->stddev = 0;
		} else {
			tree->mean = 0;
			tree->stddev = 0;
		}
	} else {
		printf("record does not exit");
	}
}
