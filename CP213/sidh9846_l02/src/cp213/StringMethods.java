package cp213;

/**
 * Sample string methods.
 *
 * @author Manveer Sidhu (169029846)
 * @version 2022-05-06
 */
public class StringMethods {
    // Constants
    /**
     * String of vowels.
     */
    public static final String VOWELS = "aeiouAEIOU";

    /**
     * Counts the number of vowels in a string. Does not include 'y'.
     *
     * @param string A string.
     * @return Number of vowels in string.
     */
    public static int vowelCount(final String string) {
	int count = 0;

	// your code here
	
		for (int i = 0; i < string.length(); i++) {
			if (VOWELS.indexOf(string.charAt(i)) != -1) {
				count++;
			}
		}
	

	return count;
    }

    /**
     * Counts the number of digits in a string.
     *
     * @param string A string.
     * @return Number of digits in string.
     */
    public static int digitCount(final String string) {
	int count = 0;

	// your code here
	
		for (int i = 0; i < string.length(); i++) {
			if (Character.isDigit(string.charAt(i))) {
				count++;
			}
		}
	

	return count;
    }

    /**
     * Totals the individual digits in a string.
     *
     * @param string A string.
     * @return The integer total of all individuals digits in string.
     */
    public static int totalDigits(final String string) {
	int total = 0;

	// your code here
	
		for (int i = 0; i < string.length(); i++) {
			if (Character.isDigit(string.charAt(i))) {
				total += Character.getNumericValue(string.charAt(i));
			}
		}

	return total;
    }

    /**
     * Compares string1 and string2 and returns a comma-delimited concatenated
     * string consisting of the string that is first lexically followed by the
     * string that is second lexically. If the strings are equal, then only string1
     * is returned.
     *
     * @param string1 String to compare against string2.
     * @param string2 String to compare against string1.
     * @return A concatenation of string1 and string2 in order.
     */
    public static String pairs(String string1, String string2) {
	String line = null;

	// your code here
	
		int compareLex = string1.compareTo(string2);
		
		if (compareLex == 0) {
			line = string1;
		} else if (compareLex < 0) {
			line = string1 + ',' + string2;
		} else if (compareLex > 0) {
			line = string2 + ',' + string1;
		}
		

	return line;
    }

    /**
     * Finds the distance between the s1 and s2. The distance between two strings of
     * the same length is the number of positions in the strings at which their
     * characters are different. If two strings are not the same length, the
     * distance is unknown (-1). If the distance is zero, then two strings are
     * equal.
     *
     * @param string1 String to compare against string2.
     * @param string2 String to compare against string1.
     * @return The distance between string1 and string2.
     */
    public static int stringDistance(String string1, String string2) {
	int distance = 0;

	// your code here
	
		int length = string1.length();
		
		if (length != string2.length()) {
			return -1;
		}
		
		for (int i = 0; i < length; i++) {
			char char1 = string1.charAt(i);
			char char2 = string2.charAt(i);
			if (char1 != char2) {
				distance++;
			}
		}
		

	return distance;
    }
}
