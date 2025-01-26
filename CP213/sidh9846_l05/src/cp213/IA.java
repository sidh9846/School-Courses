package cp213;

/**
 * Inherited class in simple example of inheritance / polymorphism.
 *
 * @author  Manveer Sidhu (169029846)
 * @version 2022-02-25
 */
public class IA extends Student {

	// your code here

	private String course = null;

	/**
	 * @param lastName  Student last name (surname): defined in Person
     * @param firstName Student first name (given name): defined in Person
     * @param id        Student id number (student id) : defined in Student
	 * @param course	Student course
	 */
	public IA(String lastName, String firstName, String id, String course) {
		super(lastName, firstName, id);
		this.course = course;
	}
	
	/**
	 * Getter for course.
	 * 
	 * @return this.course
	 */
	public String getCourse() {
		return this.course;
	}

	/**
	 *Creates formatted string version of IA.
	 */
	@Override
    public String toString() {
    	return (super.toString() + "\nCourse:" + this.course);
    }
}
