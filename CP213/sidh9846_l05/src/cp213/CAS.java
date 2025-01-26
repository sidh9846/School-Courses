package cp213;

/**
 * Inherited class in simple example of inheritance / polymorphism.
 *
 * @author Manveer Sidhu (169029846)
 * @version 2022-02-25
 */
public class CAS extends Professor {

	// your code here
	
	String term = null;

	/**
	 * @param lastName   Professor last name (surname): defined in Person
	 * @param firstName  Professor first name (given name): defined in Person
	 * @param department Professor department (department): defined in Professor
	 * @param term       Six digit string, year followed by two digits to represent the term: "01" for Winter, "05" for Spring, and "09" for Fall.
	 */
	public CAS(String lastName, String firstName, String department, String term) {
		super(lastName, firstName, department);
		
		this.term = term;
	}
	
	/**
	 * Getter for term
	 * 
	 * @return this.term
	 */
	public String getTerm() {
		return this.term;
	}

	/**
	 * Creates formatted string version of CAS.
	 */
	@Override
    public String toString() {
		return (super.toString() + "\nTerm: " + this.term);
	}
	

}
