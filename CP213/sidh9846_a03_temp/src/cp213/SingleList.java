package cp213;

/**
 * A single linked list structure of <code>Node T</code> objects. These data
 * objects must be Comparable - i.e. they must provide the compareTo method.
 * Only the <code>T</code> value contained in the priority queue is visible
 * through the standard priority queue methods. Extends the
 * <code>SingleLink</code> class.
 *
 * @author your name, id, email here
 * @version 2023-09-06
 * @param <T> this SingleList data type.
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of key in this SingleList. Private helper
     * methods - used only by other ADT methods.
     *
     * @param key The value to look for.
     * @return A pointer to the node previous to the node containing key.
     */
    private SingleNode<T> linearSearch(final T key) {

	// your code here
    	
    	SingleNode<T> current = this.front;
    	SingleNode<T> prev = null;
    	
    	while (current != null && !current.getItem().equals(key)) {
    		prev = current;
    		current = current.getNext();
    	}
    	
    	if (current == null) {
    		prev = null;
    	}

	return prev;
    }

    /**
     * Appends data to the end of this SingleList.
     *
     * @param data The value to append.
     */
    public void append(final T data) {

	// your code here
    	
    	SingleNode<T> node = new SingleNode<>(data, null);
    	
    	if (this.length == 0) {
    		this.front = node;
    		this.rear = this.front;
    	} else {
    		this.rear.setNext(node);
    		this.rear = node;
    	}
    	
    	this.length++;

	return;
    }

    /**
     * Removes duplicates from this SingleList. The list contains one and only one
     * of each value formerly present in this SingleList. The first occurrence of
     * each value is preserved.
     */
    public void clean() {

	// your code here
    	
    	SingleNode<T> current = this.front;
    	
    	while (current != null) {
    		SingleNode<T> current2 = current;
    		while (current2.getNext() != null) {
                if (current2.getNext().getItem().equals(current.getItem())) {
                	current2.setNext(current2.getNext().getNext());
                } else {
                	current2 = current2.getNext();
                }
    		}
    		current = current.getNext();
    	}

	return;
    }

    /**
     * Combines contents of two lists into a third. Values are alternated from the
     * origin lists into this SingleList. The origin lists are empty when finished.
     * NOTE: data must not be moved, only nodes.
     *
     * @param left  The first list to combine with this SingleList.
     * @param right The second list to combine with this SingleList.
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {

	// your code here
    	
    	while (!left.isEmpty() && !right.isEmpty()) {
    		this.moveFrontToRear(left);
    		this.moveFrontToRear(right);
    	}
    	
    	while (!left.isEmpty()) {
    		this.moveFrontToRear(left);
    	}
    	
    	while (!right.isEmpty()) {
    		this.moveFrontToRear(right);
    	}

	return;
    }

    /**
     * Determines if this SingleList contains key.
     *
     * @param key The key value to look for.
     * @return true if key is in this SingleList, false otherwise.
     */
    public boolean contains(final T key) {

	// your code here
    	
    	// DOES NOT WORK
    	
    	for(T data : this) {
    		if (data.equals(key)) {
    			return true;
    		}
    	}

	return false;
    }

    /**
     * Finds the number of times key appears in list.
     *
     * @param key The value to look for.
     * @return The number of times key appears in this SingleList.
     */
    public int count(final T key) {

	// your code here
    	
    	SingleNode<T> current = this.front;
    	int count = 0;
    	
    	while (current != null) {
    		if (current.getItem().equals(key)) {
                count++;
            }
    		current = current.getNext();
    	}
    	

	return count;
    }

    /**
     * Finds and returns the value in list that matches key.
     *
     * @param key The value to search for.
     * @return The value that matches key, null otherwise.
     */
    public T find(final T key) {

	// your code here
    	
    	SingleNode<T> value = linearSearch(key);
    	
    	if (value != null) {
    		return value.getNext().getItem();
    	} else {
    		return null;
    	}

    }

    /**
     * Get the nth item in this SingleList.
     *
     * @param n The index of the item to return.
     * @return The nth item in this SingleList.
     * @throws ArrayIndexOutOfBoundsException if n is not a valid index.
     */
    public T get(final int n) throws ArrayIndexOutOfBoundsException {

	// your code here
    	
    	if (n < 0 || n >= this.length) {
            throw new ArrayIndexOutOfBoundsException(n + "is not a valid index.");
        }

        SingleNode<T> current = this.front;
        int index = 0;

        while (current != null && n > index) {
            current = current.getNext();
            index++;
        }

    return current.getItem();
    	
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source The list to compare against this SingleList.
     * @return true if this SingleList contains the same values in the same order as
     *         source, false otherwise.
     */
    public boolean identical(final SingleList<T> source) {

	// your code here
    	
    	 if (this.length != source.length) {
    		 return false;
    	 }

    	 SingleNode<T> currentThis = this.front;
    	 SingleNode<T> currentSource = source.front;
    	 
    	 while (currentThis != null && currentSource != null) {
    		 if (!currentThis.getItem().equals(currentSource.getItem())) {
    	            return false;
    	        } else {
    	        	currentThis = currentThis.getNext();
    	        	currentSource = currentSource.getNext();
    	        }
    	 }
    	

	return true;
    }

    /**
     * Finds the first location of a value by key in this SingleList.
     *
     * @param key The value to search for.
     * @return The index of key in this SingleList, -1 otherwise.
     */
    public int index(final T key) {

	// your code here
    	
    	int index = 0;
    	SingleNode<T> current = this.front;
    	
    	while (current != null) {
    		if (current.getItem().equals(key)) {
    			return index;
    		} else {
    			index++;
    			current = current.getNext();
    		}
    		
    	}
    	

	return -1;
    }

    /**
     * Inserts value into this SingleList at index i. If i greater than the length
     * of this SingleList, append data to the end of this SingleList.
     *
     * @param i    The index to insert the new data at.
     * @param data The new value to insert into this SingleList.
     */
    public void insert(int i, final T data) {

	// your code here
    	
    	if (i > this.length) {
    		SingleNode<T> node = new SingleNode<>(data, null);
    		this.rear.setNext(node);
    		this.rear = node;
    	} else if (i <= 0) {
    		SingleNode<T> node = new SingleNode<>(data, this.front);
    		this.front = node;
    	} else {
            SingleNode<T> current = this.front;
            int index = 0;

            while (current != null && index < i - 1) {
                current = current.getNext();
                index++;
            }

            SingleNode<T> node = new SingleNode<>(data, current.getNext());
            current.setNext(node);
        }
    	
    	this.length++;

	return;
    }

    /**
     * Creates an intersection of two other SingleLists into this SingleList. Copies
     * data to this SingleList. left and right SingleLists are unchanged. Values
     * from left are copied in order first, then values from right are copied in
     * order.
     *
     * @param left  The first SingleList to create an intersection from.
     * @param right The second SingleList to create an intersection from.
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {

	// your code here
    	
    	SingleNode<T> currentLeft = left.front;

        while (currentLeft != null) {
            T item = currentLeft.getItem();
            if (right.contains(item) && !contains(item)) {
                insert(length, item);
            }
            currentLeft = currentLeft.getNext();
        }

	return;
    }

    /**
     * Finds the maximum value in this SingleList.
     *
     * @return The maximum value.
     */
    public T max() {

	// your code here
    	
    	T maximum = this.front.getItem();
    	SingleNode<T> current = this.front;
    	
    	while (current != null) {
    		if (maximum.compareTo(current.getItem()) < 0) {
    			maximum = current.getItem();
    		}
    		current = current.getNext();
    	}

	return maximum;
    }

    /**
     * Finds the minimum value in this SingleList.
     *
     * @return The minimum value.
     */
    public T min() {

	// your code here
    	
    	
    	T minimum = this.front.getItem();
    	SingleNode<T> current = this.front;
    	
    	while (current != null) {
    		if (minimum.compareTo(current.getItem()) > 0) {
    			minimum = current.getItem();
    		}
    		current = current.getNext();
    	}
    	

	return minimum;
    }

    /**
     * Inserts value into the front of this SingleList.
     *
     * @param data The value to insert into the front of this SingleList.
     */
    public void prepend(final T data) {

	// your code here
    	
    	if (this.length == 0) {
    		SingleNode<T> node = new SingleNode<>(data, null);
    		this.front = node;
    		this.rear = this.front;
    	} else {
	    	SingleNode<T> node = new SingleNode<>(data, this.front);
	    	this.front = node;
    	}
    	
    	this.length++;

	return;
    }

    /**
     * Finds, removes, and returns the value in this SingleList that matches key.
     *
     * @param key The value to search for.
     * @return The value matching key, null otherwise.
     */
    public T remove(final T key) {

	// your code here
    	
    	SingleNode<T> prev = linearSearch(key);

        if (prev == null) {
            if (this.front != null && this.front.getItem().equals(key)) {
                this.front = this.front.getNext();
                
                if (this.front == null) {
                    this.rear = null;
                }
            } else {
                return null;
            }
        } else {

	        SingleNode<T> current = prev.getNext();
	
	        if (current == null) {
	            this.rear = prev;
	        } else {
	        	prev.setNext(current.getNext());
	        }
        
        }
       
        
    this.length--;
    return key;
    }

    /**
     * Removes the value at the front of this SingleList.
     *
     * @return The value at the front of this SingleList.
     */
    public T removeFront() {

	// your code here

    	if (length == 0) {
    		return null;
    	}
    	
    	T value = this.front.getItem();
    	
    	this.front = this.front.getNext();
    	
    	if (this.front == null) {
    		this.rear = this.front;
    	}
    	
    	this.length--;
    	

	return value;
    }

    /**
     * Finds and removes all values in this SingleList that match key.
     *
     * @param key The value to search for.
     */
    public void removeMany(final T key) {

	// your code here
    	
    	SingleNode<T> current = this.front;
        SingleNode<T> prev = null;
        int count = 0;
        
        while (current != null) {
            if (current.getItem().equals(key)) {
                if (prev != null) {
                	prev.setNext(current.getNext());
                } else {
                	this.front = current.getNext();
                }
                
                if (current.getNext() == null) {
                    this.rear = prev;
                }
            } else {
                prev = current;
            }
            current = current.getNext();
        }
        
        
        current = this.front;
        
        while (current != null) {
            current = current.getNext();
            count++;
        }
        
        this.length = count;
        
        if (this.length == 0) {
        	this.front = null;
        	this.rear = this.front;
        }


	return;
    }

    /**
     * Reverses the order of the values in this SingleList.
     */
    public void reverse() {

	// your code here
    	
    	SingleNode<T> current = this.front;
    	SingleNode<T> next = null;
    	SingleNode<T> prev = null;

        while (current != null) {
            next = current.getNext();
            current.setNext(prev);
            prev = current;
            current = next;
        }

        this.front = prev;
        this.rear = this.front;

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. The first half of this
     * SingleList is moved to left, and the last half of this SingleList is moved to
     * right. If the resulting lengths are not the same, left should have one more
     * item than right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {

	// your code here
    	
    	SingleNode<T> current = this.front;
    	SingleNode<T> prev = null;
    	int index = 0;

        int mid = this.length / 2;
        if (this.length % 2 != 0) {
        	mid++;
        }

        while (current != null) {
            if (mid <= index) {
            	right.insert(right.length, current.getItem());
            	prev.setNext(current.getNext());
            	current = prev;
            } else {
            	left.insert(left.length, current.getItem());
            }

            prev = current;
            current = current.getNext();
            index++;
        }

        this.front = null;
        this.rear = this.front;
        this.length = 0;

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. this SingleList is empty when done. Nodes are moved alternately
     * from this SingleList to left and right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {

	// your code here
    	
    	SingleNode<T> current = this.front;
	    SingleNode<T> currentLeft = null;
	    SingleNode<T> currentRight = null;
	    boolean flipFlop = true;

	    while (current != null) {
	        SingleNode<T> node = new SingleNode<>(current.getItem(), null);

	        if (flipFlop) {
	            if (currentLeft != null) {
	            	currentLeft.setNext(node);
	            	currentLeft = currentLeft.getNext();
	            } else {
	            	left.front = node;
	            	currentLeft = left.front;
	            }
	        } else {
	            if (currentRight != null) {
	            	currentRight.setNext(node);
	            	currentRight = currentRight.getNext();
	            } else {
	            	right.front = node;
	            	currentRight = right.front;
	            }
	        }

	        flipFlop = !flipFlop;
	        current = current.getNext();
	    }

	    this.front = null;
	    this.rear = this.front;
	    this.length = 0;
    }

    /**
     * Creates a union of two other SingleLists into this SingleList. Copies value
     * to this list. left and right SingleLists are unchanged. Values from left are
     * copied in order first, then values from right are copied in order.
     *
     * @param left  The first SingleList to create a union from.
     * @param right The second SingleList to create a union from.
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {

	// your code here
    	
    	SingleNode<T> currentLeft = left.front;
        SingleNode<T> currentRight = right.front;

        // Iterate through the left list and add unique elements to the result list
        while (currentLeft != null) {
            if (contains(currentLeft.getItem())) {
            	currentLeft = currentLeft.getNext();
            } else {
            	insert(length, currentLeft.getItem());
            }
        }

        // Iterate through the right list and add unique elements to the result list
        while (currentRight != null) {
            if (contains(currentRight.getItem())) {
            	currentRight = currentRight.getNext();
            } else {
            	insert(length, currentRight.getItem());
            }
        }

	return;
    }
}
