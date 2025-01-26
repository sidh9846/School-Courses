package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author your name here
 * @author David Brown
 * @version 2023-09-06
 */
public class AVL<T extends Comparable<T>> extends BST<T> {

    /**
     * Returns the balance item of node. If greater than 1, then left heavy, if less
     * than -1, then right heavy. If in the range -1 to 1 inclusive, the node is
     * balanced. Used to determine whether to rotate a node upon insertion.
     *
     * @param node The TreeNode to analyze for balance.
     * @return A balance number.
     */
    private int balance(final TreeNode<T> node) {

	// your code here
    	
    	if (node == null) {
    		return 0;
    	} else {
    		
    		int left = 0;
    		int right = 0;
    		
    		if (node.getLeft() != null) {
    			left = node.getLeft().getHeight();
    		}
    		
    		if (node.getRight() != null) {
    			right = node.getRight().getHeight();
    		} 	
    		
    		return left - right;
    	}
    	
    }

    /**
     * Rebalances the current node if its children are not balanced.
     *
     * @param node the node to rebalance
     * @return replacement for the rebalanced node
     */
    private TreeNode<T> rebalance(TreeNode<T> node) {

	// your code here
    	
    	TreeNode<T> currentNode = node;
    	int weight = balance(node);

    	if (node != null) {
    	    if (weight > 1) {
	    		TreeNode<T> leftNode = node.getLeft();
	    		if (leftNode != null) {
	    		    int leftWeight = balance(leftNode);
	    		    if (leftWeight < 0) {
	    			node.setLeft(rotateLeft(leftNode));
	    		    }
	    		    currentNode = rotateRight(node);
	    		} else {
	    		    currentNode = rotateRight(node);
	    		}
    	    } else if (weight < -1) {
	    		TreeNode<T> rightNode = node.getRight();
	    		if (rightNode != null) {
	    		    int rightWeight = balance(rightNode);
	    		    if (rightWeight > 0) {
	    		    	node.setRight(rotateRight(rightNode));
	    		    }
	    		    currentNode = rotateLeft(node);
	    		} else {
	    		    currentNode = rotateLeft(node);
	    		}
    	    }

    	}
    	return currentNode;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> node) {

	// your code here
    	
    	if (node == null || node.getRight() == null) {
            return node;
        } else {
            TreeNode<T> newNode = node.getRight();
            node.setRight(newNode.getLeft());
            newNode.setLeft(node);

            node.updateHeight();
            newNode.updateHeight();

            return newNode;
        }

    }

    /**
     * Performs a right rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> node) {

	// your code here
    	
    	if (node == null || node.getLeft() == null) {
            return node;
        } else {

	        TreeNode<T> newNode = node.getLeft();
	        node.setLeft(newNode.getRight());
	        newNode.setRight(node);
	
	        node.updateHeight();
	        newNode.updateHeight();
	
	        return newNode;
        
        }

    }

    /**
     * Auxiliary method for insert. Inserts data into this AVL.
     *
     * @param node The current node (TreeNode).
     * @param data Data to be inserted into the node.
     * @return The inserted node.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> data) {

	// your code here
    	
    	TreeNode<T> currentNode = node;
    	
    	if (currentNode == null) {
    	    currentNode = new TreeNode<T>(data);
    	}

    	int compare = data.compareTo(currentNode.getdata());

    	if (compare < 0) {
    	    currentNode.setLeft(insertAux(currentNode.getLeft(), data));
    	} else if (compare > 0) {
    	    currentNode.setRight(insertAux(currentNode.getRight(), data));
    	} else {
    	    currentNode.getdata().incrementCount();
    	}

    	currentNode.updateHeight();
    	currentNode = rebalance(currentNode);

    	return currentNode;
    	
//        if (node == null) {
//            return new TreeNode<>(data);
//        }
//
//        int comparison = data.compareTo(node.getdata());
//
//        if (comparison < 0) {
//            node.setLeft(insertAux(node.getLeft(), data));
//        } else if (comparison > 0) {
//            node.setRight(insertAux(node.getRight(), data));
//        } else {
//            return node;
//        }
//
//        node.updateHeight();
//        
//        
//        int balance = balance(node);
//
//        // Left heavy
//        if (balance > 1) {
//            if (data.compareTo(node.getLeft().getdata()) < 0) {
//                return rotateRight(node);
//            } else {
//                node.setLeft(rotateLeft(node.getLeft()));
//                return rotateRight(node);
//            }
//        }
//        // Right heavy
//        else if (balance < -1) {
//            if (data.compareTo(node.getRight().getdata()) > 0) {
//                return rotateLeft(node);
//            } else {
//                node.setRight(rotateRight(node.getRight()));
//                return rotateLeft(node);
//            }
//        }
//
//        return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An AVL must meet the BST validation conditions, and additionally be
     * balanced in all its subtrees - i.e. the difference in height between any two
     * children must be no greater than 1.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {

	// your code here
    	
    	// Base case: An empty tree is valid
        if (node == null) {
            return true;
        } else {
	        if ((minNode == null || node.getdata().compareTo(minNode.getdata()) > 0) && (maxNode == null || node.getdata().compareTo(maxNode.getdata()) < 0)) {
	            boolean vaildLeft = isValidAux(node.getLeft(), minNode, node);
	            boolean validRight = isValidAux(node.getRight(), node, maxNode);
	
	            boolean balanced = Math.abs(balance(node)) <= 1;
	
	            return vaildLeft && validRight && balanced;
	        }
	        return false;
        }

    }

    /**
     * Determines whether two AVLs are identical.
     *
     * @param target The AVL to compare this AVL against.
     * @return true if this AVL and target contain nodes that match in position,
     *         item, count, and height, false otherwise.
     */
    public boolean equals(final AVL<T> target) {
	return super.equals(target);
    }

}
