package cp213;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.print.PrinterException;
import java.awt.print.PrinterJob;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

/**
 * The GUI for the Order class.
 *
 * @author your name here
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2023-09-06
 */
@SuppressWarnings("serial")
public class OrderPanel extends JPanel {

	// Attributes
	private Menu menu = null; // Menu attached to panel.
	private final Order order = new Order(); // Order to be printed by panel.
	// GUI Widgets
	private final JButton printButton = new JButton("Print");
	private final JLabel subtotalLabel = new JLabel("0");
	private final JLabel taxLabel = new JLabel("0");
	private final JLabel totalLabel = new JLabel("0");

	private JLabel nameLabels[] = null;
	private JLabel priceLabels[] = null;
	// TextFields for menu item quantities.
	private JTextField quantityFields[] = null;

	/**
	 * Displays the menu in a GUI.
	 *
	 * @param menu The menu to display.
	 */
	public OrderPanel(final Menu menu) {
		this.menu = menu;
		this.nameLabels = new JLabel[this.menu.size()];
		this.priceLabels = new JLabel[this.menu.size()];
		this.quantityFields = new JTextField[this.menu.size()];
		this.layoutView();
		this.registerListeners();
	}

	/**
	 * Implements an ActionListener for the 'Print' button. Prints the current
	 * contents of the Order to a system printer or PDF.
	 */
	private class PrintListener implements ActionListener {

		@Override
		public void actionPerformed(final ActionEvent e) {

			// your code here
			PrinterJob print = PrinterJob.getPrinterJob();

			print.setPrintable(order);

			try {
				if (print.printDialog())
					print.print();
			} catch (PrinterException e1) {
				// TODO Auto-generated catch block
				System.err.println(e1);
			}

		}
	}

	/**
	 * Implements a FocusListener on a JTextField. Accepts only positive integers,
	 * all other values are reset to 0. Adds a new MenuItem to the Order with the
	 * new quantity, updates an existing MenuItem in the Order with the new
	 * quantity, or removes the MenuItem from the Order if the resulting quantity is
	 * 0.
	 */
	private class QuantityListener implements FocusListener {
		private MenuItem item = null;

		QuantityListener(final MenuItem item) {
			this.item = item;
		}

		// your code here

		@Override
		public void focusGained(FocusEvent e) {
			// TODO Auto-generated method stub

		}

		@Override
		public void focusLost(FocusEvent e) {
			JTextField field = (JTextField) e.getSource();
			String text = field.getText();

			try {
				int quantity = Integer.parseInt(text);

				if (quantity < 0) {
					field.setText("0");
					quantity = 0;
				}

				order.update(item, quantity);
				updateLabels();
			} catch (NumberFormatException ex) {
				field.setText("0");
			}
		}
	}

	/**
	 * Layout the panel.
	 */
	private void layoutView() {
		// your code here

		setLayout(new BorderLayout());

		this.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

		updateLabels();

		JPanel menuPanel = new JPanel(new GridLayout(menu.size(), 3));
		JPanel summaryPanel = new JPanel(new GridLayout(4, 2));

		for (int i = 0; i < menu.size(); i++) {
			MenuItem item = menu.getItem(i);

			nameLabels[i] = new JLabel(item.getName());
			priceLabels[i] = new JLabel(String.format("$%.2f", item.getPrice())); // Format with $ sign
			quantityFields[i] = new JTextField("0");
			quantityFields[i].addFocusListener(new QuantityListener(item));

			menuPanel.add(nameLabels[i]);
			menuPanel.add(priceLabels[i]);
			menuPanel.add(quantityFields[i]);
		}

		summaryPanel.add(new JLabel("Subtotal:                 $"));
		summaryPanel.add(subtotalLabel);
		summaryPanel.add(new JLabel("Tax:                        $"));
		summaryPanel.add(taxLabel);
		summaryPanel.add(new JLabel("Total:                      $"));
		summaryPanel.add(totalLabel);
		summaryPanel.add(new JSeparator(SwingConstants.HORIZONTAL));
		summaryPanel.add(printButton);

		add(menuPanel, BorderLayout.CENTER);
		add(summaryPanel, BorderLayout.SOUTH);
	}

	/**
	 * Register the widget listeners.
	 */
	private void registerListeners() {
		// Register the PrinterListener with the print button.
		this.printButton.addActionListener(new PrintListener());

		// your code here

	}

	private void updateLabels() {
		subtotalLabel.setText(String.valueOf(order.getSubTotal()));
		taxLabel.setText(String.valueOf(order.getTaxes()));
		totalLabel.setText(String.valueOf(order.getTotal()));
	}
}