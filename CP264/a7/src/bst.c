/*
 -------------------------------------
 File:    bst.c
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
#include <string.h>
#include "bst.h"

BSTNODE* new_bstnode(RECORD data);
BSTNODE* extract_smallest_node(BSTNODE **rootp);

BSTNODE* bst_search(BSTNODE *root, char *key) {
// your code

	while (root) {
		if (strcmp(key, root->data.name) == 0)
			return root;
		else if (strcmp(key, root->data.name) < 0)
			root = root->left;
		else
			root = root->right;
	}
	return NULL;

}

void bst_insert(BSTNODE **rootp, RECORD data) {
// your code
	if (*rootp == NULL) {
		*rootp = new_bstnode(data);
	} else {
		BSTNODE *tnp = *rootp;
		while (1) {
			if (strcmp(data.name, tnp->data.name) == 0) {
				break;
			} else if (strcmp(data.name, tnp->data.name) < 0) {
				if (tnp->left == NULL) {
					tnp->left = new_bstnode(data);
					break;
				} else
					tnp = tnp->left;
			} else {
				if (tnp->right == NULL) {
					tnp->right = new_bstnode(data);
					break;
				} else
					tnp = tnp->right;
			}
		}
	}
}

void bst_delete(BSTNODE **rootp, char *key) {
// your code

	BSTNODE *tnp, *parentp, *suc, *psuc, *ptr;
	if (*rootp == NULL) {
		return; // Tree is empty, nothing to delete
	} else {
		// Find the node with the given key
		parentp = NULL;
		tnp = *rootp;
		while (tnp != NULL && strcmp(key, tnp->data.name) != 0) {
			parentp = tnp;
			tnp = (strcmp(key, tnp->data.name) < 0) ? tnp->left : tnp->right;
		}

		// If node with key not found, return
		if (tnp == NULL) {
			return;
		}

		// Determine the child node to attach to the parent
		if (tnp->left == NULL) {
			ptr = tnp->right;
		} else if (tnp->right == NULL) {
			ptr = tnp->left;
		} else {
			// Find the smallest node in the right subtree
			psuc = tnp;
			suc = tnp->right;
			while (suc->left != NULL) {
				psuc = suc;
				suc = suc->left;
			}

			// Adjust pointers to remove the successor node
			if (tnp == psuc) {
				suc->left = tnp->left;
			} else {
				psuc->left = suc->right;
				suc->left = tnp->left;
				suc->right = tnp->right;
			}
			ptr = suc;
		}

		// Attach ptr to the parent node
		if (parentp == NULL) {
			*rootp = ptr;
		} else if (parentp->left == tnp) {
			parentp->left = ptr;
		} else {
			parentp->right = ptr;
		}

		free(tnp);
	}

}

BSTNODE* new_bstnode(RECORD data) {
	BSTNODE *np = (BSTNODE*) malloc(sizeof(BSTNODE));
	if (np) {
		memcpy(np, &data, sizeof(BSTNODE));
		np->left = NULL;
		np->right = NULL;
	}
	return np;
}

BSTNODE* extract_smallest_node(BSTNODE **rootp) {
	BSTNODE *p = *rootp, *parent = NULL;
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

void clean_bst(BSTNODE **rootp) {
	BSTNODE *root = *rootp;
	if (root) {
		if (root->left)
			clean_bst(&root->left);
		if (root->right)
			clean_bst(&root->right);
		free(root);
	}
	*rootp = NULL;
}
