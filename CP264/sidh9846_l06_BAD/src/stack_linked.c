/**
 * -------------------------------------
 * @file  stack_linked.c
 * Linked Stack Source Code File
 * -------------------------------------
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2023-10-27
 *
 * -------------------------------------
 * DO NOT CHANGE CONTENTS
 */
// Includes
#include "stack_linked.h"

// Functions

// Initializes a stack.
void stack_initialize(stack_linked_struct **stack, data_type_copy copy, data_type_string to_string,
        data_type_destroy destroy) {
    *stack = malloc(sizeof **stack);
    assert((*stack) != NULL);
    (*stack)->top = NULL;
    (*stack)->copy = copy;
    (*stack)->to_string = to_string;
    (*stack)->destroy = destroy;
    return;
}

// Destroys a stack.
void stack_destroy(stack_linked_struct **source) {
    // Free the linked data
    while((*source)->top != NULL) {
        stack_node *temp = (*source)->top;
        (*source)->destroy(&(temp->item));
        (*source)->top = (*source)->top->next;
        free(temp);
        temp = NULL;
    }
    // Free the stack header
    free(*source);
    *source = NULL;
    return;
}

// Determines if a stack is empty.
bool stack_empty(const stack_linked_struct *source) {
    return (source->top == NULL);
}

// Determines if a stack is full.
bool stack_full(const stack_linked_struct *source) {
    return false;
}

// Pushes a copy of an item onto a stack.
bool stack_push(stack_linked_struct *source, const data_type *item) {
    bool pushed = false;
    stack_node *node = malloc(sizeof *node);

    if(node != NULL) {
        node->item = malloc(sizeof *node->item);

        if(node->item != NULL) {
            source->copy(node->item, item);
            node->next = source->top;
            source->top = node;
            pushed = true;
        }
    }
    return pushed;
}

// Returns a copy of the item on the top of a stack, stack is unchanged.
bool stack_peek(const stack_linked_struct *source, data_type *item) {
    bool peeked = false;

    if(source->top != NULL) {
        source->copy(item, source->top->item);
        peeked = true;
    }
    return peeked;
}

// Removes and returns the item on the top of a stack.
bool stack_pop(stack_linked_struct *source, data_type *item) {
    bool popped = false;

    if(source->top != NULL) {
        source->copy(item, source->top->item);
        stack_node *temp = source->top;
        source->top = source->top->next;
        free(temp);
        popped = true;
    }
    return popped;
}

// Prints the items in a stack from top to bottom.
void stack_print(const stack_linked_struct *source) {
    char string[DATA_STRING_SIZE];
    stack_node *current = source->top;

    while(current != NULL) {
        printf("%s\n", source->to_string(string, DATA_STRING_SIZE, current->item));
        current = current->next;
    }
    return;
}

/**
 * Recursively copies contents of ptr to node.
 *
 * @param copy - data copy function
 * @param ptr - pointer to a stack node
 * @return = pointer to a new stack node
 */
static stack_node* copy_aux(data_type_copy copy, stack_node *ptr) {
    stack_node *node = NULL;

    if(ptr != NULL) {
        node = malloc(sizeof *node);
        node->item = malloc(sizeof node->item);
        copy(node->item, ptr->item);
        node->next = copy_aux(copy, ptr->next);
    }
    return node;
}

// Copies source to target.
void stack_copy(stack_linked_struct **target, const stack_linked_struct *source) {
    *target = malloc(sizeof **target);

    (*target)->copy = source->copy;
    (*target)->to_string = source->to_string;
    (*target)->destroy = source->destroy;
    (*target)->top = copy_aux(source->copy, source->top);
    return;
}

/**
 * Moves the top node of a source stack to a target stack.
 *
 * @param target - pointer to target stack
 * @param source - pointer to source stack
 */
static void stack_move_top(stack_linked_struct *target, stack_linked_struct *source) {
    assert(source->top != NULL);

    stack_node *temp = source->top;
    source->top = source->top->next;
    temp->next = target->top;
    target->top = temp;
    return;
}

// Combines the contents of two source stacks into a target stack.
void stack_combine(stack_linked_struct *target, stack_linked_struct *source1, stack_linked_struct *source2) {

    while(source1->top != NULL && source2->top != NULL) {
        stack_move_top(target, source1);
        stack_move_top(target, source2);
    }
    while(source1->top != NULL) {
        stack_move_top(target, source1);
    }
    while(source2->top != NULL) {
        stack_move_top(target, source2);
    }
    return;
}

// Splits a source stack alternately into two target stacks.
void stack_split_alt(stack_linked_struct *target1, stack_linked_struct *target2, stack_linked_struct *source) {
    bool left = true;

    while(source->top != NULL) {

        if(left) {
            stack_move_top(target1, source);
        } else {
            stack_move_top(target2, source);
        }
        left = !left;
    }
    return;
}

