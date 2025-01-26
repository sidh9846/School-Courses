/**
 * -------------------------------------
 * @file  main.c
 * Lab 5 Main Source Code File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2023-10-01
 *
 * -------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>

#include "data.h"
#include "queue_linked.h"
#include "stack_linked.h"

#define SIZE 128

/**
 * Simple stack testing.
 */
void test_stack(void) {
	char buffer[SIZE];
	data_type item = 0;
	stack_linked_struct *stack = NULL;
	stack_initialize(&stack, data_copy, data_to_string, data_destroy);

	// your code here

	printf("TEST STACK:\n");

	stack_push(stack, &item);

	data_type item1 = 1;
	stack_push(stack, &item1);

	data_type item2 = 2;
	stack_push(stack, &item2);

	data_type item3 = 3;
	stack_push(stack, &item3);

	stack_print(stack);

	data_type peeked = 0;
	stack_peek(stack, &peeked);

	printf("Peek: %i\n", peeked);

	data_type popped = 0;
	stack_pop(stack, &popped);

	printf("Pop: %i\n", popped);

	data_type popped1 = 0;
	stack_pop(stack, &popped1);

	printf("Pop: %i\n", popped1);

	stack_destroy(&stack);

	printf("---");
}

/**
 * Simple queue testing.
 */
void test_queue(void) {
	char buffer[SIZE];
	data_type item = 0;
	queue_linked_struct *queue = NULL;
	queue_initialize(&queue, data_copy, data_to_string, data_destroy);

// your code here

	queue_destroy(&queue);
}

/**
 * Test the file and string functions.
 *
 * @param argc - unused
 * @param args - unused
 * @return EXIT_SUCCESS
 */
int main(int argc, char *argv[]) {
	setbuf(stdout, NULL);

	test_stack();
	test_queue();

	return (EXIT_SUCCESS);
}
