package cp213;

import java.util.Scanner;

/**
 * Class to demonstrate the use of Scanner with a keyboard and File objects.
 *
 * @author Manveer Sidhu (169026846)
 * @version 2022-01-08
 */
public class ScannerTest {

    /**
     * Count lines in the scanned file.
     *
     * @param source Scanner to process
     * @return number of lines in scanned file
     */
    public static int countLines(final Scanner source) {
		int count = 0;
	
		// your code here
		
		while(source.hasNextLine()) {
			count++;
			source.nextLine();
		}
	
		return count;
    }

    /**
     * Count tokens in the scanned object.
     *
     * @param source Scanner to process
     * @return number of tokens in scanned object
     */
    public static int countTokens(final Scanner source) {
		int tokens = 0;
	
		// your code here
		
		while(source.hasNextLine()) {
			while(source.hasNext()) {
				tokens++;
				source.next();
			}
			source.nextLine();
		}
	
		return tokens;
    }

    /**
     * Ask for and total integers from the keyboard.
     *
     * @param keyboard Scanner to process
     * @return total of positive integers entered from keyboard
     */
    public static int readNumbers(final Scanner keyboard) {
		int total = 0;
	
		// your code here
		
		
		while (true) {
			if (keyboard.hasNextInt()) {
				total += keyboard.nextInt();
			} else {
				String input = keyboard.next();
				if (!input.equals("q")) {
					System.out.println("'" + input + "' is not an integer or 'q'.");
				} else {
					break;
				}
			}
		}
		
//		String input = keyboard.next();
//		
//		while (!input.equals("q")) {
//			//boolean isInt = true;
//			
////			try {
////		        Integer.parseInt(input);
////		    } catch (NumberFormatException nfe) {
////		        isInt = false;
////		    }
//
//			boolean isInt = keyboard.hasNextInt();
//			
//			if (isInt) {
//				total += keyboard.nextInt();//Integer.parseInt(input);
//				input = keyboard.next();
//			} 
//			else {
//				input = keyboard.next();
//				if (!input.equals("q")) {
//					System.out.println("'" + input + "' is not an integer or 'q'.");
//				}
//			}
//			
//		}		
		return total;
    }


}
