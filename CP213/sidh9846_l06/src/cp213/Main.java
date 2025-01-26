package cp213;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    /**
     * @param args unused
     */
    public static void main(String[] args) {
	System.out.println("Test scannerTest");
	System.out.println();
	Scanner keyboard = new Scanner(System.in);
	int total = scannerTest(keyboard);
	keyboard.close();
	System.out.println("Total: " + total);
	System.out.println();

	System.out.print("Test stringPrinter");
	System.out.println();

	try {
	    String output = stringPrinter(5, "*");
	    System.out.println(output);
	    output = stringPrinter(-5, "*");
	    System.out.println(output);
	} catch (Exception e) {
	    System.out.println();
	    System.out.println("getMessage:");
	    System.out.println(e.getMessage());
	    System.out.println();
	    System.out.println("toString:");
	    System.out.println(e.toString());
	    System.out.println();
	    System.out.println("printStackTrace:");
	    e.printStackTrace();
	}
    }

    /**
     * Uses exceptions to capture bad input from a keyboard Scanner.
     *
     * @return The total of all the integers entered.
     */
    public static int scannerTest(final Scanner keyboard) {

	// your code here
    	
    	
    	int total = 0;
    	
    	String input = null;
    	   
    	while (true) {
    		
    		System.out.print("Enter an integer (\"Quit\" to stop): ");
    		
    		input = keyboard.next();
    		
    		try {
				total += Integer.valueOf(input);
			} 
    		catch (NumberFormatException e) {
				if (input.equals("Quit")) {
					return total;
				} 
				System.out.println("That is not an integer!");
    		}
			catch (InputMismatchException e) {
				if (input.equals("Quit")) {
					return total;
				} 
				System.out.println("That is not an integer!");
			}
	
		}
				
	}


    /**
     * Repeats a string.
     *
     * @param n   Number of times to repeat a string.
     * @param str The string to print.
     * @return The repeated string.
     * @throws Exception If n is negative.
     */
    public static String stringPrinter(int n, String str) throws Exception {

	// your code here
    	
    	String string = "";
    	
    	if (n < 0) {
    		throw new Exception("Please Enter a Positive Number!");
    	}
    	
    	for (int i = 0; i < n; i++) {
    		string += str;
    	}
    	

	return string;
    }

}
