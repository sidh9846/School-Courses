package cp213;

import java.util.Scanner;

/**
 * Wraps around an Order object to ask for MenuItems and quantities.
 *
 * @author your name here
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2023-09-06
 */
public class Cashier {

	// Attributes
	private Menu menu = null;

	/**
	 * Constructor.
	 *
	 * @param menu A Menu.
	 */
	public Cashier(Menu menu) {
		this.menu = menu;
	}

	/**
	 * Prints the menu.
	 */
	private void printCommands() {
		System.out.println("\nMenu:");
		System.out.println(menu.toString());
		System.out.println("Press 0 when done.");
		System.out.println("Press any other key to see the menu again.\n");
	}

	/**
	 * Asks for commands and quantities. Prints a receipt when all orders have been
	 * placed.
	 *
	 * @return the completed Order.
	 */
	public Order takeOrder() {
		System.out.println("Welcome to WLU Foodorama!");

		// your code here

		System.out.println("Welcome to WLU Foodorama!");


        Order order = new Order();

        Scanner scanner = new Scanner(System.in);
        String userInput;

        printCommands();

        do {

            System.out.print("Command: ");
            userInput = scanner.nextLine();

            if ("0".equals(userInput)) {
                break;
            }

            try {
                int itemNumber = Integer.parseInt(userInput);
                if (itemNumber > 0 && itemNumber <= menu.size()) {
                    MenuItem menuItem = menu.getItem(itemNumber - 1);

                    System.out.print("How many do you want? ");
                    int quantity = scanner.nextInt();
                    scanner.nextLine();

                    order.add(menuItem, quantity);
                } else {
                	printCommands();
                }
            } catch (NumberFormatException e) {
                System.out.println("Not a valid number");
                printCommands();
            }
        } while (true);

        System.out.println("\nOrder Summary:");
        System.out.println(order.toString());

        return order;
	}
}