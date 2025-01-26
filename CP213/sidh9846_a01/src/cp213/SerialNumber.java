package cp213;

import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author Your name and id here
 * @version 2023-05-23
 */
public class SerialNumber {

    /**
     * Determines if a string contains all digits.
     *
     * @param str The string to test.
     * @return true if str is all digits, false otherwise.
     */
    public static boolean allDigits(final String str) {

	// your code here
    	
    	int length = str.length();
    	
    	for (int i = 0; i < length; i++) {
    		char testChar = str.charAt(i);
    		if (!Character.isDigit(testChar)) {
    			return false;
    		}
    	}
    	
    	

	return true;
    }

    /**
     * Determines if a string is a good serial number. Good serial numbers are of
     * the form 'SN/nnnn-nnn', where 'n' is a digit.
     *
     * @param sn The serial number to test.
     * @return true if the serial number is valid in form, false otherwise.
     */
    public static boolean validSn(final String sn) {

	// your code here
    	
    	if (sn.length() != 11) {
    		return false;
    	}
    	
    	if (!sn.startsWith("SN/")) {
    		return false;
    	}
    	if (sn.charAt(7) != '-') {
    		return false;
    	}
    	
    	try {  
    	    Integer.parseInt(sn.substring(3,7));  
    	  } catch(NumberFormatException e){  
    		  return false;  
    	  }  
    	try {  
    	    Integer.parseInt(sn.substring(8,11));  
    	  } catch(NumberFormatException e){  
    		  return false;  
    	  }  
    	

	return true;
    }

    /**
     * Evaluates serial numbers from a file. Writes valid serial numbers to
     * good_sns, and invalid serial numbers to bad_sns. Each line of fileIn contains
     * a (possibly valid) serial number.
     *
     * @param fileIn  a file already open for reading
     * @param goodSns a file already open for writing
     * @param badSns  a file already open for writing
     */
    public static void validSnFile(final Scanner fileIn, final PrintStream goodSns, final PrintStream badSns) {

	// your code here
    	

	return;
    }

}
