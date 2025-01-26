/**
 * -------------------------------------
 * @file  bst_linked.c
 * Linked BST Source Code File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2024-03-01
 *
 * -------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include "data.h"
#include "bst_linked.h"

// Macro for comparing node heights
#define MAX_HEIGHT(a,b) ((a) > (b) ? a : b)

//--------------------------------------------------------------------
// Local Static Helper Functions

/**
 * Initializes a new BST node with a copy of item.
 *
 * @param source - pointer to a BST source
 * @param item - pointer to the item to assign to the node
 * @return a pointer to a new BST node
 */
static bst_node* bst_node_initialize(const data_ptr item) {
	// Base case: add a new node containing a copy of item.
	bst_node *node = malloc(sizeof *node);
	node->item = malloc(sizeof *node->item);
	data_copy(node->item, item);
	node->height = 1;
	node->left = NULL;
	node->right = NULL;
	return node;
}

/**
 * Helper function to determine the height of node - handles empty node.
 * @param node - The node to process.
 * @return The height of the current node.
 */
static int bst_node_height(const bst_node *node) {
	int height = 0;

	if (node != NULL) {
		height = node->height;
	}
	return height;
}

/**
 * Updates the height of a node. Its height is the max of the heights of its
 * child nodes, plus 1.
 * @param node The node to process.
 */
static void bst_update_height(bst_node *node) {
	int left_height = bst_node_height(node->left);
	int right_height = bst_node_height(node->right);

	node->height = MAX_HEIGHT(left_height, right_height) + 1;
	return;
}

/**
 * Inserts item into a BST. Insertion must preserve the BST definition.
 * item may appear only once in source.
 *
 * @param source - pointer to a BST
 * @param node - pointer to a node
 * @param item - the item to insert
 * @return - TRUE if item inserted, FALSE otherwise
 */
static BOOLEAN bst_insert_aux(bst_linked *source, bst_node **node,
		const data_ptr item) {
	BOOLEAN inserted = FALSE;

	if (*node == NULL) {
		// Base case: add a new node containing the item.
		*node = bst_node_initialize(item);
		source->count += 1;
		inserted = TRUE;
	} else {
		// Compare the node data_ptr against the new item.
		int comp = data_compare(item, (*node)->item);

		if (comp < 0) {
			// General case: check the left subsource.
			inserted = bst_insert_aux(source, &(*node)->left, item);
		} else if (comp > 0) {
			// General case: check the right subsource.
			inserted = bst_insert_aux(source, &(*node)->right, item);
		}
	}
	if (inserted) {
		// Update the node height if any of its children have been changed.
		bst_update_height(*node);
	}
	return inserted;
}

//--------------------------------------------------------------------
// Functions

// Initializes a BST.
bst_linked* bst_initialize() {
	bst_linked *source = malloc(sizeof *source);
	source->root = NULL;
	source->count = 0;
	return source;
}

// frees a BST.
void bst_free(bst_linked **source) {

	// your code here

	return;
}

// Determines if a BST is empty.
BOOLEAN bst_empty(const bst_linked *source) {

	// your code here

	return (source->count == 0);
}

// Determines if a BST is full.
BOOLEAN bst_full(const bst_linked *source) {
	return FALSE;
}

// Returns number of items in a BST.
int bst_count(const bst_linked *source) {

	// your code here

	return source->count;
}

static void bst_inorder_aux(const bst_node *node, data_ptr *items, int *index) {

	if (node != NULL) {

		bst_inorder_aux(node->left, items, index);
		items[*index] = node->item;
		(*index)++;
		bst_inorder_aux(node->right, items, index);

	}

	return;
}

// Copies the contents of a BST to an array in inorder.
void bst_inorder(const bst_linked *source, data_ptr *items) {

	// your code here

	if (source == NULL || source->root == NULL)
		return;

	int index = 0;
	bst_inorder_aux(source->root, items, &index);

	return;
}

// Copies the contents of a BST to an array in preorder.
void bst_preorder(const bst_linked *source, data_ptr *items) {

	// your code here

	return;
}

// Copies the contents of a BST to an array in postorder.
void bst_postorder(const bst_linked *source, data_ptr *items) {

	// your code here

	return;
}

// Inserts a copy of an item into a BST.
BOOLEAN bst_insert(bst_linked *source, const data_ptr item) {
	return bst_insert_aux(source, &(source->root), item);
}

// Retrieves a copy of a value matching key in a BST.
BOOLEAN bst_retrieve(bst_linked *source, const data_ptr key, data_ptr item) {

	// your code here

	BOOLEAN found = FALSE;
	bst_node *curr = malloc(sizeof curr);

	if (source->root == NULL)
		return FALSE;

	curr = source->root;

	while (!found && curr != NULL) {
		if (data_compare(curr->item, key) == 0) {
			found = TRUE;
		} else if (data_compare(curr->item, key) > 0) {
			if (curr->left == NULL)
				break;
			curr = curr->left;
		} else if (data_compare(curr->item, key) < 0) {
			if (curr->right == NULL)
				break;
			curr = curr->right;
		}
	}

	if (found) {
		data_copy(item, key);
		return TRUE;
	}

	return FALSE;
}

// Removes a value matching key in a BST.
BOOLEAN bst_remove(bst_linked *source, const data_ptr key, data_ptr item) {

// your code here

	return FALSE;
}

// Copies source to target.
void bst_copy(bst_linked **target, const bst_linked *source) {

// your code here

}

// Finds the maximum item in a BST.
BOOLEAN bst_max(const bst_linked *source, data_ptr item) {

// your code here

	return FALSE;
}

// Finds the minimum item in a BST.
BOOLEAN bst_min(const bst_linked *source, data_ptr item) {

// your code here

	return FALSE;
}

// Function to count leaf nodes in the BST
static int bst_leaf_count_aux(const bst_node *node) {

	if (node == NULL)
		return 0;

	if (node->left == NULL && node->right == NULL)
		return 1;

	return bst_leaf_count_aux(node->left) + bst_leaf_count_aux(node->right);
}

// Finds the number of leaf nodes in a tree.
int bst_leaf_count(const bst_linked *source) {

// your code here

	if (source == NULL || source->root == NULL)
		return 0;

	return bst_leaf_count_aux(source->root);
}

// Finds the number of nodes with one child in a tree.
int bst_one_child_count(const bst_linked *source) {

// your code here

	return 0;
}

// Finds the number of nodes with two children in a tree.
int bst_two_child_count(const bst_linked *source) {

// your code here

	return 0;
}

// Determines the number of nodes with zero, one, and two children.
// (May not call bst_leaf_count, bst_one_child_count, or bst_two_child_count.)
void bst_node_counts(const bst_linked *source, int *zero, int *one, int *two) {

// your code here

	return;
}

static BOOLEAN bst_balanced_aux(bst_node *node, BOOLEAN *balanced) {
	if (node == NULL)
		return FALSE;

	int left_height = bst_balanced_aux(node->left, balanced);
	if (!balanced)
		return FALSE;

	int right_height = bst_balanced_aux(node->right, balanced);
	if (!balanced)
		return FALSE;

	if (abs(left_height - right_height) > 1) {
		*balanced = FALSE;
		return FALSE;
	}

	return node->height;
}
// Determines whether or not a tree is a balanced tree.
BOOLEAN bst_balanced(const bst_linked *source) {

// your code here

	BOOLEAN balanced = TRUE;

	if (bst_empty(source)) {
		return balanced;
	} else {
		bst_balanced_aux(source->root, &balanced);
		return balanced;
	}

	return FALSE;
}

// Determines whether or not a tree is a valid BST.
BOOLEAN bst_valid(const bst_linked *source) {

// your code here

	return FALSE;
}

// Determines if two trees contain same data in same configuration.
BOOLEAN bst_equals(const bst_linked *target, const bst_linked *source) {

// your code here

	return FALSE;
}

/**
 * Private helper function to print contents of BS in preorder.
 *
 * @param to_string - function to print data_ptr
 * @param node - pointer to bst_node
 */
static void bst_print_aux(bst_node *node) {
	char string[DATA_STRING_SIZE];

	if (node != NULL) {
		printf("%s\n", data_string(string, DATA_STRING_SIZE, node->item));
		bst_print_aux(node->left);
		bst_print_aux(node->right);
	}
	return;
}

// Prints the items in a BST in preorder.
void bst_print(const bst_linked *source) {
	printf("  count: %d, height: %d, items:\n", source->count,
			source->root->height);
	bst_print_aux(source->root);
	printf("\n");
	return;
}
