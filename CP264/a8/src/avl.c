/*
 -------------------------------------
 File:    avl.c
 Project: a8
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-03-13
 -------------------------------------
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "avl.h"

/* Create and return AVLNODE of given data
 * Use malloc()
 * @param data - data for the new node.
 * @return - pointer to the new AVLNODE.
 */
AVLNODE* new_node(RECORD data);

/* Return the balance factor at the given node
 * @param np - pointer to the node of tree
 * @return - the balance factor a the node,
 */
int balance_factor(AVLNODE *np);

/* This function does the left rotation at a given node
 * @param np - pointer to the rotation node.
 * @return - the pointer to the replaced node.
 */
AVLNODE* rotate_left(AVLNODE *np);

/* This function does the right rotation at a given node
 * @param np - pointer to the rotation node.
 * @return - the pointer to the replaced node.
 */
AVLNODE* rotate_right(AVLNODE *root);

AVLNODE* extract_smallest_node(AVLNODE **rootp);

AVLNODE* new_node(RECORD data) {
	AVLNODE *np = (AVLNODE*) malloc(sizeof(AVLNODE));
	if (np) {
		np->data = data;
		np->height = 1;
		np->left = NULL;
		np->right = NULL;
	}
	return np;
}

int max(int a, int b) {
	return (a > b) ? a : b;
}

static void avl_rebalance(AVLNODE **node, int balance) {

	// your code here

	// Left
	if (balance > 1) {
		// Right
		if (balance_factor((*node)->left) < 0)
			(*node)->left = rotate_left((*node)->left);
		// Left
		*node = rotate_right(*node);
	}
	// Right
	else if (balance < -1) {
		// Left
		if (balance_factor((*node)->right) > 0)
			(*node)->right = rotate_right((*node)->right);
		// Right
		*node = rotate_left(*node);
	}

	return;
}

static void avl_update_height(AVLNODE *node) {
	int left_height = height(node->left);
	int right_height = height(node->right);

	if (left_height >= right_height) {
		node->height = left_height + 1;
	} else {
		node->height = right_height + 1;
	}
	return;
}

int height(AVLNODE *np) {
// your code
	int h = 0;
	if (np)
		h = np->height;
	return h;
}

int balance_factor(AVLNODE *np) {
// your code
	int b = 0;
	if (np)
		b = height(np->left) - height(np->right);
	return b;
}

AVLNODE* rotate_right(AVLNODE *y) {
// your code

	AVLNODE *new_root = y->left;
	y->left = new_root->right;
	new_root->right = y;

	avl_update_height(y);
	avl_update_height(new_root);

	return new_root;

}

AVLNODE* rotate_left(AVLNODE *x) {
// your code

	AVLNODE *new_root = x->right;
	x->right = new_root->left;
	new_root->left = x;

	// Update heights
	avl_update_height(x);
	avl_update_height(new_root);

	return new_root;
}

void avl_insert(AVLNODE **rootp, RECORD data) {
	// 1. Perform the normal BST insertion
	if (*rootp == NULL) {
		AVLNODE *np = (AVLNODE*) malloc(sizeof(AVLNODE));
		if (np) {
			np->data = data;
			np->height = 1;
			np->left = NULL;
			np->right = NULL;
		}
		*rootp = np;
	} else {

		AVLNODE *root = *rootp;

		if (strcmp(data.name, root->data.name) == 0)
			return;
		else if (strcmp(data.name, root->data.name) < 0) {
			avl_insert(&root->left, data);
		} else {
			avl_insert(&root->right, data);
		}

		// 2. update height of this ancestor node
		//root->height =
		avl_update_height(*rootp);

		// 3. Get the balance factor of this ancestor node to check whether this node became unbalanced
		int balance = balance_factor(*rootp);

		// 4. rebalance if not balanced
		avl_rebalance(rootp, balance);
	}
}

void avl_delete(AVLNODE **rootp, char *name) {
	AVLNODE *root = *rootp;
	AVLNODE *np;
	if (root == NULL)
		return;

	if (strcmp(name, root->data.name) == 0) {
		if (root->left == NULL && root->right == NULL) {
			free(root);
			*rootp = NULL;
		} else if (root->left != NULL && root->right == NULL) {
			np = root->left;
			free(root);
			*rootp = np;
		} else if (root->left == NULL && root->right != NULL) {
			np = root->right;
			free(root);
			*rootp = np;
		} else if (root->left != NULL && root->right != NULL) {
			np = extract_smallest_node(&root->right);
			np->left = root->left;
			np->right = root->right;
			free(root);
			*rootp = np;
		}
	} else {
		if (strcmp(name, root->data.name) < 0) {
			avl_delete(&root->left, name);
		} else {
			avl_delete(&root->right, name);
		}
	}

// If the tree had only one node then return
	if (*rootp == NULL)
		return;
	root = *rootp;

// STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
	//root->height =
	avl_update_height(root);

// STEP 3: GET THE BALANCE FACTOR OF THIS NODE
	int balance = balance_factor(*rootp);

// STEP 4: rebalance if not balanced
	avl_rebalance(*rootp, balance);

}

AVLNODE* avl_search(AVLNODE *root, char *name) {
// your code
	AVLNODE *node = root;

	while (node != NULL) {
		int comp = strcmp(name, node->data.name);

		if (comp < 0) {
			node = node->left;
		} else if (comp > 0) {
			node = node->right;
		} else {
			return node;
		}
	}
	return NULL;
}

AVLNODE* extract_smallest_node(AVLNODE **rootp) {
	AVLNODE *p = *rootp, *parent = NULL;
	if (p) {
		while (p->left) {
			parent = p;
			p = p->left;
		}
		if (parent == NULL)
			*rootp = p->right;
		else
			parent->left = p->right;

		p->left = NULL;
		p->right = NULL;
	}
	return p;
}
void clean_avl(AVLNODE **rootp) {
	AVLNODE *root = *rootp;
	if (root) {
		if (root->left)
			clean_avl(&root->left);
		if (root->right)
			clean_avl(&root->right);
		free(root);
	}
	*rootp = NULL;
}
