package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author your name here
 * @author David Brown
 * @version 2023-09-06
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

	/**
	 * Auxiliary method for valid. May force node rotation if the retrieval count of
	 * the located node item is incremented.
	 *
	 * @param node The node to examine for key.
	 * @param key  The item to search for. Count is updated to count in matching
	 *             node item if key is found.
	 * @return The updated node.
	 */
	private TreeNode<T> retrieveAux(TreeNode<T> node, final CountedItem<T> key) {

		// your code here

		if (node == null) {
			node = null;
		} else {
			final int value = node.getdata().compareTo(key);
			this.comparisons += 1;
			if (value > 0) {
				node.setLeft(this.retrieveAux(node.getLeft(), key));
				if (node.getLeft() != null && node.getdata().getCount() < node.getLeft().getdata().getCount()) {
					node = this.rotateRight(node);
				}
			} else if (value < 0) {
				node.setRight(this.retrieveAux(node.getRight(), key));
				if (node.getRight() != null && node.getdata().getCount() < node.getRight().getdata().getCount()) {
					node = this.rotateLeft(node);
				}
			} else {
				node.getdata().incrementCount();
				key.setCount(node.getdata().getCount());
				node.updateHeight();
			}
		}
		return node;

	







	//    	if (node == null) {
	//    		node = null;
	//    	} else {
	//    		final int value = node.getdata().compareTo(key);
	//    		this.comparisons++;
	//    		
	//    		if (value > 0) {
	//    			node.setLeft(this.retrieveAux(node.getLeft(), key));
	//    			if (node.getLeft() != null && node.getdata().getCount() < node.getLeft().getdata().getCount()) {
	//    				node = this.rotateRight(node);
	//    			}
	//    		} else if (value < 0){
	//    			node.setRight(this.retrieveAux(node.getRight(), key));
	//    			if (node.getRight() != null && node.getdata().getCount() < node.getRight().getdata().getCount()) {
	//    				node = this.rotateLeft(node);
	//    			}
	//    		} else {
	//    			node.getdata().incrementCount();
	//    			key.setCount(node.getdata().getCount());
	//    			node.updateHeight();
	//    		}
	//    	}
	//
	//    	return node;
}

/**
 * Performs a left rotation around node.
 *
 * @param parent The subtree to rotate.
 * @return The new root of the subtree.
 */
private TreeNode<T> rotateLeft(final TreeNode<T> parent) {

	// your code here
	TreeNode<T> node = parent.getRight();
	parent.setRight(node.getLeft());
	node.setLeft(parent);
	parent.updateHeight();
	node.updateHeight();

	return node;
}

/**
 * Performs a right rotation around {@code node}.
 *
 * @param parent The subtree to rotate.
 * @return The new root of the subtree.
 */
private TreeNode<T> rotateRight(final TreeNode<T> parent) {

	// your code here
	TreeNode<T> node = parent.getLeft();
	parent.setLeft(node.getRight());
	node.setRight(parent);
	parent.updateHeight();
	node.updateHeight();

	return node;

}

/**
 * Replaces BST insertAux - does not increment count on repeated insertion.
 * Counts are incremented only on retrieve.
 */
@Override
protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> data) {

	// your code here

	TreeNode<T> newNode = node;

	if (newNode == null) {
		newNode = new TreeNode<>(data);
		this.size += 1;
	} else {
		int compare = data.compareTo(node.getdata());
		if (compare < 0) {
			newNode.setLeft(this.insertAux(newNode.getLeft(), data));
		} else if (compare > 0) {
			newNode.setRight(this.insertAux(newNode.getRight(), data));
		} else {
			newNode.getdata().incrementCount();
			data.setCount(newNode.getdata().getCount());
		}
	}

	newNode.updateHeight();
	return newNode;
}

/**
 * Auxiliary method for valid. Determines if a subtree based on node is a valid
 * subtree. An Popularity Tree must meet the BST validation conditions, and
 * additionally the counts of any node data must be greater than or equal to the
 * counts of its children.
 *
 * @param node The root of the subtree to test for validity.
 * @return true if the subtree base on node is valid, false otherwise.
 */
@Override
protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {

	// your code here

	boolean valid = false;
	TreeNode<T> currentNode = node;

	if (currentNode == null) {
		valid = true;
	} else if (Math.max(this.nodeHeight(currentNode.getLeft()), this.nodeHeight(currentNode.getRight())) != currentNode.getHeight() - 1) {
		valid = false;
	} else if ((currentNode.getLeft() != null && currentNode.getLeft().getdata().compareTo(currentNode.getdata()) >= 0) || (currentNode.getRight() != null && currentNode.getRight().getdata().compareTo(currentNode.getdata()) <= 0)) {
		valid = false;
	} else if ((currentNode.getLeft() != null && currentNode.getdata().getCount() < currentNode.getLeft().getdata().getCount()) || (currentNode.getRight() != null && currentNode.getdata().getCount() < currentNode.getRight().getdata().getCount())) {
		valid = false;
	} else {
		valid = this.isValidAux(currentNode.getLeft(), minNode, maxNode) && this.isValidAux(currentNode.getRight(), minNode, maxNode);
	}

	return valid;
}

/**
 * Determines whether two PopularityTrees are identical.
 *
 * @param target The PopularityTree to compare this PopularityTree against.
 * @return true if this PopularityTree and target contain nodes that match in
 *         position, item, count, and height, false otherwise.
 */
public boolean equals(final PopularityTree<T> target) {
	return super.equals(target);
}

/**
 * Very similar to the BST retrieve, but increments the data count here instead
 * of in the insertion.
 *
 * @param key The key to search for.
 */
@Override
public CountedItem<T> retrieve(CountedItem<T> key) {

	// your code here

	CountedItem<T> data = key;

	this.root = this.retrieveAux(this.root, data);

	if (data.getCount() == 0) {
		data = null;
	} else {
		data = new CountedItem<T>(data);
	}

	return data;
}

}
