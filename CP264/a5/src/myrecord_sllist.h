/*
 -------------------------------------
 File:    myrecord_sllist.h
 Project: a5
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-15
 -------------------------------------
 */
#ifndef MYRECORD_SLLIST_H_
#define MYRECORD_SLLIST_H_

/**
 * RECORD structure
 * name  - char array for person's name
 * score - float score of record
 */
typedef struct {
	char name[20];
	float score;
} RECORD;

/**
 * NODE structure
 * data  - RECORD data
 * next  - pointer pointing to the next node of singly linked list
 */
typedef struct node {
	RECORD data;
	struct node *next;
} NODE;

/**
 * Singly linked list structure
 * int length  - the number of nodes of the linked list
 * NODE *start - pointer pointing to the first node of the linked list
 */
typedef struct sllist {
	int length;
	NODE *start;
} SLL;

/**
 * Search singly linked list by the key name.
 *
 * @param SLL *sllp - provides the address of a singly linked list structure.
 * @param char *name - key to search
 * @return Pointer to found node if found; otherwise NULL
 */
NODE* sll_search(SLL *sllp, char *name);

/**
 * Insert a new record to linked list at the position sorted by record name field.
 *
 * @param SLL *sllp - provides the address of a singly linked list structure.
 * @param char *name - name field of the new record.
 * @param float score - the score data of the new record.
 */
void sll_insert(SLL *sllp, char *name, float score);

/**
 * Delete a node of record matched by the name key from linked list.
 *
 * @param SLL *sllp provides the address of a singly linked list structure.
 * @param name - key used to find the node for deletion.
 * @return 1 if deleted a matched node, 0 otherwise.
 */
int sll_delete(SLL *sllp, char *name);

/**
 * Clean singly linked list, delete all nodes.
 * @param @param SLL *sllp provides the address of a singly linked list structure.
 */
void sll_clean(SLL *sllp);

#endif /* MYRECORD_SLLIST_H_ */
