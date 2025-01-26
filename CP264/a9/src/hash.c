/*
 -------------------------------------
 File:    hash.c
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
#include "hash.h"

HASHNODE* hashtable_search(HASHTABLE *ht, char *key) {
// your code
	int hashIndex = hash(key, ht->size);
	HASHNODE *curr = ht->hna[hashIndex];

	while (curr != NULL) {
		if (strcmp(curr->key, key) == 0) {
			return curr;
		}
		curr = curr->next;
	}

	return NULL;
}

int hashtable_insert(HASHTABLE *ht, char *key, int value) {
// your code

	int hashIndex = hash(key, ht->size);
	HASHNODE *curr = ht->hna[hashIndex];
	HASHNODE *prev = NULL;

	while (curr != NULL) {
		if (strcmp(curr->key, key) == 0) {
			curr->value = value;
			return 0;
		}
		prev = curr;
		curr = curr->next;
	}

	HASHNODE *newNode = (HASHNODE*) malloc(sizeof(HASHNODE));

	strcpy(newNode->key, key);
	newNode->value = value;
	newNode->next = NULL;

	if (prev == NULL) {
		ht->hna[hashIndex] = newNode;
	} else {
		prev->next = newNode;
	}

	ht->count++;

	return 1;

}

int hashtable_delete(HASHTABLE *ht, char *key) {
// your code

	int hashIndex = hash(key, ht->size);
	HASHNODE *curr = ht->hna[hashIndex];
	HASHNODE *prev = NULL;
	int found = 0;

	while (curr != NULL && !found) {
		if (strcmp(curr->key, key) == 0) {
			found = 1;
			break;
		}
		prev = curr;
		curr = curr->next;
	}

	if (found) {
		if (prev == NULL) {
			ht->hna[hashIndex] = curr->next;
		} else {
			prev->next = curr->next;
		}

		ht->count--;
		return 1;
	}

	return 0;
}

int hash(char *key, int size) {
	unsigned int hash = 0;
	while (*key) {
		hash += *key++;
	}
	return hash % size;
}

HASHTABLE* new_hashtable(int size) {
	HASHTABLE *ht = (HASHTABLE*) malloc(sizeof(HASHTABLE));
	ht->hna = (HASHNODE**) malloc(sizeof(HASHNODE**) * size);
	int i;
	for (i = 0; i < size; i++)
		*(ht->hna + i) = NULL;

	ht->size = size;
	ht->count = 0;
	return ht;
}

void hashtable_clean(HASHTABLE **htp) {
	if (*htp == NULL)
		return;
	HASHTABLE *ht = *htp;
	HASHNODE *p, *temp;
	int i;
	for (i = 0; i < ht->size; i++) {
		p = ht->hna[i];
		while (p) {
			temp = p;
			p = p->next;
			free(temp);
		}
		ht->hna[i] = NULL;
	}
	free(ht->hna);
	ht->hna = NULL;
	*htp = NULL;
}
