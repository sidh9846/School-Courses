"""
-------------------------------------------------------
Linked version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy


class _Stack_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a stack node that contains a copy of value
        and a link to the next node in the stack.
        Use: node = _Stack_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Stack node (_Stack_Node)
        Returns:
            a new _Stack_Node object (_Stack_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Values are stored in a 
        linked structure.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._top = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        # your code here
        return

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"

        # your code here
        return

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot peek at an empty stack"

        # your code here
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

	def _move_top(self, source):
        """
        -------------------------------------------------------
        Moves the top node from the source stack to the target stack.
        The target stack contains the old top node of the source stack.
        The source stack top is updated. Equivalent of
        self.push(source.pop()), but moves nodes, not data.
        Use: target._move_top(source)
        -------------------------------------------------------
        Parameters:
            source - a linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._top is not None, "Cannot move the top of an empty stack"

        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked stack (Stack)
            source2 - an linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            _value - the next value in the stack (?)
        -------------------------------------------------------
        """
        current = self._top

        while current is not None:
            yield current._value
            current = current._next
