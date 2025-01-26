"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-17"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from Queue_array import Queue


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        # your code here
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    # Given from lab
    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here

        value = None
        pointer = self._root

        while pointer is not None and value is None:
            if key == pointer._value:
                value = deepcopy(pointer._value)
            elif key < pointer._value:
                pointer = pointer._left
            elif key > pointer._value:
                pointer = pointer._right

        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        # your code here
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                pass
                # your code here

            elif node._left is None:
                # node has no left child.
                pass
                # your code here

            elif node._right is None:
                # node has no right child.
                pass
                # your code here

            else:
                # Node has two children
                pass
                # your code here

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        # your code here
        return

    def remove_root(self):
        """
        -------------------------------------------------------
        Removes the root node and returns its value.
        Use: value = bst._remove_root()
        -------------------------------------------------------
        Returns:
            value - value in root.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove the room of an empty BST"

        # your code here

        value = self._root._value

        # Case 1: The root has no children.
        if self._root._left is None and self._root._right is None:
            self._root = None
        # Case 2: The root has one child.
        elif self._root._left is None:
            self._root = self._root._right
        elif self._root._right is None:
            self._root = self._root._left
        # Case 3: The root has two children.
        else:
            new_root = self.max()
            new_root = 
            self._root._value = new_root._value
            self.remove(new_root._value)

        self._count -= 1

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here

        contains = True

        if self.retrieve(key) is None:
            contains = False

        return contains

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        # your code here
        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return

    def parent_i(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # your code here
        return

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # your code here
        return

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here

        # while node._right is not None:
        #     node = node._right
        # return node

        lst = []
        node = self._root

        self._inorder_aux(node, lst)

        value = deepcopy(lst[-1])

        return value

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here
        return

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here

        # while node._left is not None:
        #     node = node._left
        # return node

        lst = []
        node = self._root

        self._inorder_aux(node, lst)

        value = deepcopy(lst[0])

        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here
        return

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        # your code here

        count = 0

        count = self._leaf_count_aux(self._root, count)

        return count

    def _leaf_count_aux(self, node, count):

        if node is None:
            pass
        elif node._left is None and node._right is None:
            count += 1
        elif node._left is not None and node._right is not None:
            count = self._leaf_count_aux(node._left, count)
            count = self._leaf_count_aux(node._right, count)
        elif node._left is not None:
            count = self._leaf_count_aux(node._left, count)
        elif node._right is not None:
            count = self._leaf_count_aux(node._right, count)

        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        count = 0

        count = self._two_child_count_aux(self._root, count)

        return count

    def _two_child_count_aux(self, node, count):

        if node is None:
            pass
        elif node._left is not None and node._right is not None:
            count += 1
        if node is None:
            pass
        elif node._left is not None and node._right is not None:
            count = self._two_child_count_aux(node._left, count)
            count = self._two_child_count_aux(node._right, count)
        elif node._left is not None:
            count = self._two_child_count_aux(node._left, count)
        elif node._right is not None:
            count = self._two_child_count_aux(node._right, count)

        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        # your code here
        count = 0

        count = self._one_child_count_aux(self._root, count)

        return count

    def _one_child_count_aux(self, node, count):

        if node is None:
            pass
        elif node._left is None and node._right is not None:
            count += 1
        elif node._left is not None and node._right is None:
            count += 1
        if node is None:
            pass
        elif node._left is not None and node._right is not None:
            count = self._one_child_count_aux(node._left, count)
            count = self._one_child_count_aux(node._right, count)
        elif node._left is not None:
            count = self._one_child_count_aux(node._left, count)
        elif node._right is not None:
            count = self._one_child_count_aux(node._right, count)

        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        # your code here

        node = self._root

        count_zero = 0
        count_zero = self._leaf_count_aux(node, count_zero)

        count_one = 0
        count_one = self._one_child_count_aux(node, count_one)

        count_two = 0
        count_two = self._two_child_count_aux(node, count_two)

        return count_zero, count_one, count_two

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # your code here

        return

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        # your code here
        return

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        # your code here
        return

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # your code here

        ### DOES NOT FACTOR IN HEIGHT ###

        valid = True
        lst = []

        self._inorder_aux(self._root, lst)

        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                valid = False

        # if self._root is not None:
        #     valid = self._is_valid_aux(self._root, valid)

        return valid

    # def _is_valid_aux(self, node, valid):
    #
    #     if node is None:
    #         pass
    #     elif node._left is not None and node._right is not None:
    #         valid = self._is_valid_aux(
    #             node._left, valid) and self._is_valid_aux(node._right, valid)
    #     elif node._left is None:
    #         valid = self._is_valid_aux(node._right, valid)
    #     elif node._right is None:
    #         valid = self._is_valid_aux(node._left, valid)
    #     elif node._left._value >= node._right._value:
    #         return False
    #
    #     return valid

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        # your code here

        lst = []

        self._inorder_aux(self._root, lst)

        return lst

    def _inorder_aux(self, node, lst):
        if node is not None:
            self._inorder_aux(node._left, lst)
            lst.append(node._value)
            self._inorder_aux(node._right, lst)

        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        # your code here

        lst = []

        self._preorder_aux(self._root, lst)

        return lst

    def _preorder_aux(self, node, lst):
        if node is not None:
            lst.append(node._value)
            self._preorder_aux(node._left, lst)
            self._preorder_aux(node._right, lst)

        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        # your code here

        lst = []

        self._postorder_aux(self._root, lst)

        return lst

    def _postorder_aux(self, node, lst):
        if node is not None:
            self._postorder_aux(node._left, lst)
            self._postorder_aux(node._right, lst)
            lst.append(node._value)

        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        # your code here

        lst = []
        queue = Queue()
        queue.insert(self._root)

        while self._root is not None and len(queue) > 0:
            node = queue.remove()
            lst.append(node._value)
            if node._left is not None:
                queue.insert(node._left)
            if node._right is not None:
                queue.insert(node._right)

        return lst

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """
        # your code here

        number = self._count_aux(self._root)

        return number

    def _count_aux(self, node):

        count = 0

        if node is None:
            count = 0
        else:
            count = 1 + self._count_aux(node._left) + \
                self._count_aux(node._right)

        return count

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
