package cp213;

/**
 * @author Manveer Sidhu (169029846)
 * @version 2023-05-23
 */
public class Cipher {
    // Constants
    public static final String ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static final int ALPHA_LENGTH = ALPHA.length();

    /**
     * Encipher a string using a shift cipher. Each letter is replaced by a letter
     * 'n' letters to the right of the original. Thus for example, all shift values
     * evenly divisible by 26 (the length of the English alphabet) replace a letter
     * with itself. Non-letters are left unchanged.
     *
     * @param s string to encipher
     * @param n the number of letters to shift
     * @return the enciphered string in all upper-case
     */
    public static String shift(final String s, final int n) {

	// your code here
    	
    	// postion + n % 26
    	
    	String newString = "";
    	
    	int length = s.length();
    	
    	for (int i = 0; i < length; i++) {
    		char currentChar = s.charAt(i);
    		
    		if (Character.isAlphabetic(currentChar)) {
	    		int index = ALPHA.indexOf(currentChar);
	    		int newIndex = (index + n) % ALPHA_LENGTH;
	    		char newChar = ALPHA.charAt(newIndex);
	    		
	    		newString = newString.concat(String.valueOf(newChar));
	    		
    		} else {
    			newString = newString.concat(String.valueOf(currentChar));
    		}
    		
    	}
    	

	return newString;
    }

    /**
     * Encipher a string using the letter positions in ciphertext. Each letter is
     * replaced by the letter in the same ordinal position in the ciphertext.
     * Non-letters are left unchanged. Ex:
     *
     * <pre>
    Alphabet:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Ciphertext: AVIBROWNZCEFGHJKLMPQSTUXYD
     * </pre>
     *
     * A is replaced by A, B by V, C by I, D by B, E by R, and so on. Non-letters
     * are ignored.
     *
     * @param s          string to encipher
     * @param ciphertext ciphertext alphabet
     * @return the enciphered string in all upper-case
     */
    public static String substitute(final String s, final String ciphertext) {

	// your code here
    	
    	String newString = "";
    	
    	int length = s.length();
    	
    	for (int i = 0; i < length; i++) {
    		char currentChar = s.charAt(i);
    		
    		if (Character.isAlphabetic(currentChar)) {
    			int index = ALPHA.indexOf(currentChar);
	    		char newChar = ciphertext.charAt(index);
	    		
	    		newString = newString.concat(String.valueOf(newChar));
    		} else {
    			newString = newString.concat(String.valueOf(currentChar));
    		}
    	}
    	
    	

	return newString;
    }

}
