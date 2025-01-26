package cp213;

import java.time.LocalDate;

/**
 * Student class definition.
 *
 * @author Manveer Sidhu (169029846)
 * @version 2022-01-17
 */
public class Student implements Comparable<Student> {

    // Attributes
    private LocalDate birthDate = null;
    private String forename = "";
    private int id = 0;
    private String surname = "";

    /**
     * Instantiates a Student object.
     *
     * @param id        student ID number
     * @param surname   student surname
     * @param forename  name of forename
     * @param birthDate birthDate in 'YYYY-MM-DD' format
     */
    public Student(int newId, String newSurname, String newForename, LocalDate newBirthDate) {

	// assign attributes here
    	
    	birthDate = newBirthDate;
        forename = newForename;
        id = newId;
        surname = newSurname;

	return;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of student data.
     */
    @Override
    public String toString() {
	String string = "";

	// your code here
	
	string = "Name:      " + surname + ", " + forename + "\n";
	string += "ID:        " + Integer.toString(id) + "\n";
	string += "Birthdate: " + birthDate;

	return string;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Student target) {
	int result = 0;

	// your code here
	
	int surnameCompare = surname.compareTo(target.surname);
	int forenameCompare = forename.compareTo(target.forename);
	int idCompare = Integer.compare(id, target.id);
			
	
	if (surnameCompare == 0) {
		if (forenameCompare == 0) {
			if (idCompare == 0) {
				result = 0;
			} else if (idCompare < 0) {
				result = -1;
			} else if (idCompare > 0) {
				result = 1;
			}
		} else if (forenameCompare < 0) {
			result = -1;
		} else if (forenameCompare > 0) {
			result = 1;
		}
	} else if (surnameCompare < 0) {
		result = -1;
	} else if (surnameCompare > 0) {
		result = 1;
	}

	
	return result;
    }


    // getters and setters defined here
    
    
    // setters
    
    /**
     * Sets new surname of student
     * 
     * @param newSurname	new surname of student
     */
    public void setSurname(String newSurname) {
    	
    	surname = newSurname;
    	
    	return;
    }
    
    /**
     * Sets new forename of student
     * 
     * @param newForename	new forename of student
     */
    public void setForename(String newForename) {
    	
    	forename = newForename;
    	
    	return;
    }
    
    /**
     * Sets new birthDate of student
     * 
     * @param newBirthdate	new birthDate of student
     */
    public void setBirthDate(LocalDate newBirthdate) {
    	
    	birthDate = newBirthdate;
    	
    	return;
    }
    
    /**
     * Sets new id of student
     * 
     * @param newId	  new id of student
     */
    public void setId(int newId) {
    	
    	id = newId;
    	
    	return;
    }
    
    
    // getters
    
    
    /**
     * Gets current surname of student
     * 
     * @return current surname of student
     */
    public String getSurname() {
    	
    	return surname;
    	
    }
    
    /**
     * Gets current forename of student
     * 
     * @return current forename of student
     */
    public String getForename() {
    	
    	return forename;
    }
    
    /**
     * Gets current birthDate of student
     * 
     * @return current birthDate of student
     */
    public LocalDate getBirthDate( ) {

    	return birthDate;
    }
    
    /**
     * Gets current id of student
     * 
     * @return current id of student
     */
    public int getId() {
    	
    	return id;
    }


}
