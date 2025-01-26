package cp213;

import java.time.LocalDate;

/**
 * Tests the Student class.
 *
 * @author Manveer Sidhu (169029846)
 * @version 2022-01-17
 */
public class Main {

    public static void main(String[] args) {
	final String line = "-".repeat(40);
	int id = 123456;
	String surname = "Brown";
	String forename = "David";
	LocalDate birthDate =  LocalDate.parse("1962-10-25");
	Student student = new Student(id, surname, forename, birthDate);
	System.out.println("New Student:");
	System.out.println(student);
	System.out.println(line);
	System.out.println("Test Getters");

	// call getters here
	
	System.out.println(student.getSurname());
	System.out.println(student.getForename());
	System.out.println(student.getId());
	System.out.println(student.getBirthDate());
	

	System.out.println(line);
	System.out.println("Test Setters");

	// call setters here

	System.out.println("Updated Student:");
	System.out.println(student);
	System.out.println(line);
	System.out.println("Test compareTo");

	// create new Students - call comparisons here
	
	Student student2 = new Student(id+246, surname+"ing", forename+"son", birthDate);
	
	System.out.println(student.compareTo(student2));
	System.out.println(student.compareTo(student));
	System.out.println(student2.compareTo(student));
	
    }

}
