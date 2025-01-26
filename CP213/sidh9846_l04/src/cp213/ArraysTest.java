package cp213;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Arrays Lab task methods.
 *
 * @author Manveer Sidhu (168029846)
 * @version 2022-01-25
 */
public class ArraysTest {

    /**
     * Tests arrays.
     *
     * @param args unused default parameter
     */
    public static void main(final String[] args) {
	System.out.println("Task 1");
	System.out.println(ArraysTest.task1());
	System.out.println("Task 2");
	System.out.println(ArraysTest.task2());
	System.out.println("Task 3");
	System.out.println(ArraysTest.task3());
	System.out.println("Task 4");
	System.out.println(ArraysTest.task4());
	System.out.println("Task 5");
	System.out.println(Arrays.toString(ArraysTest.task5()));
    }

    /**
     * Print the contents of the arrays first and second using a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task1() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;

	// your code here
	
		for (int i = 0; i < first.length; i++) {
			System.out.println(first[i]);
			System.out.println(second[i]);
		}

	// return true; - or - return false;
		
	return true;
    }

    /**
     * Double the contents of the array first with a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task2() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;

	// your code here
	
	for (int i = 0; i < first.length; i++) {
		first[i] *= 2;
	}
	

	// return true; - or - return false;
	
	return true;
    }

    /**
     * Double the contents of the array first with an enhanced for loop.
     *
     * @return true if the values in first are permanently changed, false otherwise
     */
    public static boolean task3() {
	final int[] first = { 1, 3, 5, 7, 9 };

	// your code here
	
		for (int i: first) {
			i *= 2;
		}
	

	// return true; - or - return false;
	return false;
    }

    /**
     * Attempt to assign the array first to a row of the 2D array third.
     *
     * @return true if this is allowed, false otherwise
     */
    public static boolean task4() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[][] third = new int[1][];

		// your code here
	
		third[0] = first;
//		System.out.println(third[0]);
//		System.out.println(first);

		// return true; - or - return false;
	return true;
    }

    /**
     * Assign the values 1 through 10 to an Integer ArrayList.
     *
     * @return the contents of the ArrayList as an Integer[] array.
     */
    public static Integer[] task5() {
	final ArrayList<Integer> values = new ArrayList<>();

	// your code here
		
		for (int i = 0; i < 10; i++) {
			values.add(i);
		}
	
		Integer[] valuesArray = values.toArray(new Integer[0]);
	
	return valuesArray;
    }
}
