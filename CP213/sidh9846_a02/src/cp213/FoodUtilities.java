package cp213;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Utilities for working with Food objects.
 *
 * @author your name, id, email here
 * @version 2023-05-07
 */
public class FoodUtilities {

    /**
     * Determines the average calories in a list of foods. No rounding necessary.
     * Foods list parameter may be empty.
     *
     * @param foods a list of Food
     * @return average calories in all Food objects
     */
    public static int averageCalories(final ArrayList<Food> foods) {

	// your code here
    	
    	int length = foods.size();
    	int totalCals = 0;
    	int avgCals = 0;
    	
    	if (length != 0) {
	    	for (int i = 0; i < length; i++) {
	    		totalCals += foods.get(i).getCalories();
	    	}
	    	avgCals = (int) (totalCals / length);
    	}
    	

	return avgCals;
    }

    /**
     * Determines the average calories in a list of foods for a particular origin.
     * No rounding necessary. Foods list parameter may be empty.
     *
     * @param foods  a list of Food
     * @param origin the origin of the Food
     * @return average calories for all Foods of the specified origin
     */
    public static int averageCaloriesByOrigin(final ArrayList<Food> foods, final int origin) {

	// your code here

    	ArrayList<Food> foodList = new ArrayList<Food>();
    	foodList = foods;
    	
    	foodList = getByOrigin(foodList, origin);
    	int avgCal = averageCalories(foodList);
    	

	return avgCal;
    }

    /**
     * Creates a list of foods by origin.
     *
     * @param foods  a list of Food
     * @param origin a food origin
     * @return a list of Food from origin
     */
    public static ArrayList<Food> getByOrigin(final ArrayList<Food> foods, final int origin) {

	// your code here
    	
    	ArrayList<Food> originFoods = new ArrayList<Food>();
    	
    	int length = foods.size();
    	
    	for (int i = 0; i < length; i++) {
    		if (foods.get(i).getOrigin() == origin) {
    			originFoods.add(foods.get(i));
    		}
    	}

	return originFoods;
    }

    /**
     * Creates a Food object by requesting data from a user. Uses the format:
     *
     * <pre>
    Name: name
    Origins
     0 Canadian
     1 Chinese
    ...
    11 English
    Origin: origin number
    Vegetarian (Y/N): Y/N
    Calories: calories
     * </pre>
     *
     * @param keyboard a keyboard Scanner
     * @return a Food object
     */
    public static Food getFood(final Scanner keyboard) {

	// your code here
    	System.out.print("Name: ");
    	String name = keyboard.nextLine();
    	
    	System.out.println(Food.originsMenu());
    	System.out.print("Origin: ");
    	int origin = keyboard.nextInt();
    	
    	keyboard.nextLine();
    	
    	System.out.print("Vegetarian (Y/N): ");
    	boolean isVegetarian = keyboard.nextLine().equalsIgnoreCase("Y")?true:false;
    	
    	System.out.print("Calories: ");
    	int calories = keyboard.nextInt();
    	
    	Food food = new Food(name, origin, isVegetarian, calories);
    	

	return food;
    }

    /**
     * Creates a list of vegetarian foods.
     *
     * @param foods a list of Food
     * @return a list of vegetarian Food
     */
    public static ArrayList<Food> getVegetarian(final ArrayList<Food> foods) {

	// your code here
    	
    	ArrayList<Food> vegFoods = new ArrayList<Food>();
    	
    	int length = foods.size();
    	
    	for (int i = 0; i < length; i++) {
    		if (foods.get(i).isVegetarian()) {
    			vegFoods.add(foods.get(i));
    		}
    	}

	return vegFoods;
    }

    /**
     * Creates and returns a Food object from a line of string data.
     *
     * @param line a vertical bar-delimited line of food data in the format
     *             name|origin|isVegetarian|calories
     * @return the data from line as a Food object
     */
    public static Food readFood(final String line) {

	// your code here
    	
    	
    	String[] info = line.split("\\|");
    	
    	String name = info[0];
    	int origin = Integer.valueOf(info[1]);
    	boolean isVegetarian = Boolean.parseBoolean(info[2]);
    	int calories = Integer.valueOf(info[3]);
    	
    	
    	Food food = new Food(name, origin, isVegetarian, calories);
    	

	return food;
    }

    /**
     * Reads a file of food strings into a list of Food objects.
     *
     * @param fileIn a Scanner of a Food data file in the format
     *               name|origin|isVegetarian|calories
     * @return a list of Food
     */
    public static ArrayList<Food> readFoods(final Scanner fileIn) {

	// your code here
    	
    	ArrayList<Food> foodList = new ArrayList<Food>();
    	
    	while (fileIn.hasNext()) {
    		String line = fileIn.nextLine();
    		Food food = readFood(line);
    		
    		foodList.add(food);
    	}
    		
    		

	return foodList;
    }

    /**
     * Searches for foods that fit certain conditions.
     *
     * @param foods        a list of Food
     * @param origin       the origin of the food; if -1, accept any origin
     * @param maxCalories  the maximum calories for the food; if 0, accept any
     * @param isVegetarian whether the food is vegetarian or not; if false accept
     *                     any
     * @return a list of foods that fit the conditions specified
     */
    public static ArrayList<Food> foodSearch(final ArrayList<Food> foods, final int origin, final int maxCalories,
	    final boolean isVegetarian) {

	// your code here
    	
    	ArrayList<Food> foodList = new ArrayList<Food>();
    	foodList = foods;
    	
    	if (origin != -1) {
    		foodList = getByOrigin(foodList, origin);
    	}
    	
    	if (isVegetarian) {
    		foodList = getVegetarian(foodList);
    	}
    	
    	if (maxCalories != 0) {
    		int length = foodList.size();
    		
    		for (int i = 0; i < length; i++) {
    			Food food = foods.get(i);
    			if (maxCalories >= food.getCalories()) {
    				foodList.remove(food);
    			}
    		}
    		
    	}
    	

	return foodList;
    }

    /**
     * Writes the contents of a list of Food to a PrintStream.
     *
     * @param foods a list of Food
     * @param ps    the PrintStream to write to
     */
    public static void writeFoods(final ArrayList<Food> foods, PrintStream ps) {

	// your code here
    	
    	for (Food f: foods) {
    		f.write(ps);
    	}

    }
}
