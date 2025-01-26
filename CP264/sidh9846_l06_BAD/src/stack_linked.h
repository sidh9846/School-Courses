/**
 * -------------------------------------
 * @file  stack_linked.h
 * Linked Stack Header File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2023-10-08
 *
 * -------------------------------------
 * DO NOT CHANGE CONTENTS
 */
#ifndef STACK_LINKED_H_
#define STACK_LINKED_H_

// Includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>
#include <assert.h>

#include "data.h"

// typedefs

/**
 * Stack node.
 */
typedef struct stack_node {
    data_type *item;          // Pointer to the node data_type .
    struct stack_node *next; // Pointer to the next stack node.
} stack_node;

/**
 * Stack header.
 */
typedef struct {
    stack_node *top;            // Pointer to the top node of the stack.
    data_type_copy copy;        // Pointer to data_type  copy function.
    data_type_string to_string; // Pointer to data_type  to string function.
    data_type_destroy destroy;  // Pointer to data_type  destroy function.
} stack_linked_struct;

// Prototypes

/**
 * Initializes a stack.
 *
 * @param stack - pointer to the stack to initialize.
 * @param copy - the data copy function
 * @param to_string - the data to_string function
 * @param destroy - the data destroy function
 */
void stack_initialize(stack_linked_struct **stack, data_type_copy copy, data_type_string to_string,
        data_type_destroy destroy);

/**
 * Destroys a stack.
 *
 * @param source - pointer to a stack
 */
void stack_destroy(stack_linked_struct **source);

/**
 * Determines if a stack is empty.
 *
 * @param source - pointer to a stack.
 * @return - true if source is empty, false otherwise
 */
bool stack_empty(const stack_linked_struct *source);

/**
 * Determines if a stack is full.
 *
 * @param source - pointer to a stack
 * @return - true if the stack is full, false otherwise
 */
bool stack_full(const stack_linked_struct *source);

/**
 * Pushes a copy of an item onto a stack.
 *
 * @param source - pointer to a stack
 * @param item - pointer to the item to push
 * @return - true if item pushed, false otherwise
 */
bool stack_push(stack_linked_struct *source, const data_type *item);

/**
 * Returns a copy of the item on the top of a stack, stack is unchanged.
 *
 * @param source - pointer to a stack
 * @param item - pointer to a copy of the item to retrieve
 * @return - true if item peeked, false otherwise (stack is empty)
 */
bool stack_peek(const stack_linked_struct *source, data_type *item);

/**
 * Removes and returns the item on the top of a stack.
 *
 * @param stack - pointer to a stack
 * @param item - pointer the item to remove
 * @return - true if item popped, false otherwise (stack is empty)
 */
bool stack_pop(stack_linked_struct *source, data_type *item);

/**
 * Prints the items in a stack from top to bottom.
 * (For testing only).
 *
 * @param stack - pointer to a stack
 */
void stack_print(const stack_linked_struct *source);

/**
 * Copies source to target.
 *
 * @param target - pointer to a stack
 * @param source - pointer to a stack
 */
void stack_copy(stack_linked_struct **target, const stack_linked_struct *source);

/**
 * Combines the contents of two source stacks into a target stack. Items alternate.
 * Source stacks are empty (not destroyed) when the function completes.
 * Moves nodes, not data.
 *
 * @param target - pointer to target stack
 * @param source1 - pointer to first source stack
 * @param source2 - pointer to second source stack
 */
void stack_combine(stack_linked_struct *target, stack_linked_struct *source1, stack_linked_struct *source2);

/**
 * Splits a source stack alternately into two target stacks. Items alternate.
 * Source stack is empty (not destroyed) when function completes.
 * Moves nodes, not data.
 *
 * @param target1 - pointer to first target stack
 * @param target2 - pointer to second target stack
 * @param source - pointer to source stack
 */
void stack_split_alt(stack_linked_struct *target1, stack_linked_struct *target2, stack_linked_struct *source);

#endif /* STACK_LINKED_H_ */
