package cp213;

import java.io.PrintStream;

/**
 * Food class definition.
 *
 * @author your name, id, email here
 * @version 2023-05-07
 */
public class Food implements Comparable<Food> {

    // Constants
    public static final String ORIGINS[] = { "Canadian", "Chinese", "Indian", "Ethiopian", "Mexican", "Greek",
	    "Japanese", "Italian", "Moroccan", "Scottish", "Columbian", "English" };

    /**
     * Creates a string of food origins in the format:
     *
     * <pre>
    Origins
    0 Canadian
    1 Chinese
    ...
    11 English
     * </pre>
     *
     * @return A formatted numbered string of valid food origins.
     */
    public static String originsMenu() {

	// your code here
    	
    	String menu = "";
    	
    	for (int i = 0; i < ORIGINS.length; i++) {
    		menu += String.format("%2d %s\n", i, ORIGINS[i]);
    	}
    	
	return menu;
    }

    // Attributes
    private String name = null;
    private int origin = 0;
    private boolean isVegetarian = false;
    private int calories = 0;

    /**
     * Food constructor.
     *
     * @param name         food name
     * @param origin       food origin code
     * @param isVegetarian whether food is vegetarian
     * @param calories     caloric content of food
     */
    public Food(final String nameInput, final int originInput, final boolean isVegetarianInput, final int caloriesInput) {

	// your code here
    	
    	name = nameInput;
    	origin = originInput;
    	isVegetarian = isVegetarianInput;
    	calories = caloriesInput;

	return;
    }

    /*
     * (non-Javadoc) Compares this food against another food.
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    /**
     * Foods are compared by name, then by origin if the names match. Must ignore
     * case.
     */
    @Override
    public int compareTo(final Food target) {

	// your code here
    	
    	int compare = 0;
    	int nameCompare = name.compareToIgnoreCase(target.name);
    	
    	if (nameCompare == 0) {
    		int originCompare = Integer.compare(origin, target.origin);
    		
    		if (originCompare == 0) {
    			return compare;
    		} else if (originCompare < 0) {
    			compare = -1;
    		} else if (originCompare > 0) {
    			compare = 1;
    		}
    		
    	} else if (nameCompare < 0) {
    		compare = -1;
    	} else if (nameCompare > 0) {
    		compare = 1;
    	}
    	
    	

	return compare;
    }

    /**
     * Getter for calories attribute.
     *
     * @return calories
     */
    public int getCalories() {

	// your code here

	return calories;
    }

    /**
     * Getter for name attribute.
     *
     * @return name
     */
    public String getName() {

	// your code here

	return name;
    }

    /**
     * Getter for origin attribute.
     *
     * @return origin
     */
    public int getOrigin() {

	// your code here

	return origin;
    }

    /**
     * Getter for string version of origin attribute.
     *
     * @return string version of origin
     */
    public String getOriginString() {

	// your code here

	return ORIGINS[origin];
    }

    /**
     * Getter for isVegetarian attribute.
     *
     * @return isVegetarian
     */
    public boolean isVegetarian() {

	// your code here
    	
    return isVegetarian;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object//toString() Creates a formatted string of food data.
     */
    /**
     * Returns a string version of a Food object in the form:
     *
     * <pre>
    Name:       name
    Origin:     origin string
    Vegetarian: true/false
    Calories:   calories
     * </pre>
     */
    @Override
    public String toString() {

	// your code here
    	
    	String food = "";
    	
    	food += String.format("Name:       %s\n", name);
    	food += String.format("Origin:     %s\n", ORIGINS[origin]);
    	food += String.format("Vegetarian: %b\n", isVegetarian);
    	food += String.format("Calories:   %d\n", calories);
    	

	return food;
    }

    /**
     * Writes a single line of food data to an open PrintStream. The contents of
     * food are written as a string in the format name|origin|isVegetarian|calories
     * to ps.
     *
     * @param ps The PrintStream to write to.
     */
    public void write(final PrintStream ps) {

	// your code here
    	
    	String line = String.format("%s|%s|%b|%d", calories, origin, isVegetarian, calories);
    	ps.println(line);
    	
	return;
    }

}
