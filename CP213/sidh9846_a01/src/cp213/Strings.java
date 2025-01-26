package cp213;

/**
 * @author Your name and id here
 * @version 2023-05-23
 */
public class Strings {
    // Constants
    public static final String VOWELS = "aeiouAEIOU";

    /**
     * Determines if string is a "palindrome": a word, verse, or sentence (such as
     * "Able was I ere I saw Elba") that reads the same backward or forward. Ignores
     * case, spaces, digits, and punctuation in the string parameter s.
     *
     * @param string a string
     * @return true if string is a palindrome, false otherwise
     */
    public static boolean isPalindrome(final String string) {

	// your code here
    
    	String cleanStr = "";
    	
    	for (int i = 0; i < string.length(); i++) {
    		if (Character.isLetter(string.charAt(i))) {
    			cleanStr = cleanStr.concat(String.valueOf(Character.toLowerCase(string.charAt(i))));
    		}
    	}
    	
    	
    	int left = 0;
    	int right = cleanStr.length() - 1;
    	
    	while (right != left || left < right) {
    		if (cleanStr.charAt(left) != cleanStr.charAt(right)) {
    			return false;
    		} else {
    			left++;
    			right--;
    		}
    	}
    	

	return true;
    }

    /**
     * Determines if name is a valid Java variable name. Variables names must start
     * with a letter or an underscore, but cannot be an underscore alone. The rest
     * of the variable name may consist of letters, numbers and underscores.
     *
     * @param name a string to test as a Java variable name
     * @return true if name is a valid Java variable name, false otherwise
     */
    public static boolean isValid(final String name) {

	// your code here
    	
    	int length = name.length();
    	
    	if ((length == 1 && name.startsWith("_")) || Character.isDigit(name.charAt(0))) {
    		return false;
    	}
    	
    	for (int i = 0; i < length; i++) {
    		char testChar = name.charAt(i);
    		if (Character.isAlphabetic(testChar) || Character.isDigit(testChar) || testChar == '_') {
    			//pass
    		} else {
    			return false;
    			
    		}
    	}

	return true;
    }

    /**
     * Converts a word to Pig Latin. The conversion is:
     * <ul>
     * <li>if a word begins with a vowel, add "way" to the end of the word.</li>
     * <li>if the word begins with consonants, move the leading consonants to the
     * end of the word and add "ay" to the end of that. "y" is treated as a
     * consonant if it is the first character in the word, and as a vowel for
     * anywhere else in the word.</li>
     * </ul>
     * Preserve the case of the word - i.e. if the first character of word is
     * upper-case, then the new first character should also be upper case.
     *
     * @param word The string to convert to Pig Latin
     * @return the Pig Latin version of word
     */
    public static String pigLatin(String word) {

	// your code here
    	
    	
    	// check if starts with vowel
    	boolean vowelStart = false;
    	
    	for (int i = 0; i < VOWELS.length(); i++) {
    		if (word.startsWith(String.valueOf(VOWELS.charAt(i)))) {
    			vowelStart = true;
    		}
    	}
    	
    	if (vowelStart) {
    		String pigLatin = word.concat("way");
    		return pigLatin;
    	}
    	
    	
    	// check if capitlized
    	boolean isUpper = false;
    	
    	if (Character.isUpperCase(word.charAt(0))) {
    		isUpper = true;
    	}
    	
    	
    	// location of first vowel
    	int index = 0;
    	
    	for (int i = 0; i < word.length(); i++) {
    		if (VOWELS.indexOf(word.charAt(i)) != -1) {
    			index = i;
    			break;
    		} 
    	}
    
    	// construct piglatin
    	String pigLatin = word.substring(index) + word.substring(0, index) + "ay";
    	
    	
    	// capitlize if needed
    	if (isUpper) {
    		pigLatin = pigLatin.substring(0, 1).toUpperCase() + pigLatin.substring(1).toLowerCase();
    	}


	return pigLatin;
    }

}
