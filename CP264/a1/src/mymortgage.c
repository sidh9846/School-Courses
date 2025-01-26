/**
 * -------------------------------------
 * @file  mymortgage.c
 * mymortgage function file
 * -------------------------------------
 * @author Manveer Sidhu, 169029846, sidh9846@mylaurier.ca
 *
 * @version 2024-01-11
 *
 * -------------------------------------
 */

#include "mymortgage.h"
#include <math.h>

/**
 * Compute the monthly payment of given mortgage princile, annual interest rate (%), and mortgage years.
 *
 * @param principal_amount - float type.
 * @param annual_interest_rate - value of parcentage rate, e.g. 5 means 5%, float type.
 * @param years - number of mortgage year, int type.
 * @return - monthly payment, float type.
 */
float monthly_payment(float principal_amount, float annual_interest_rate,
		int years) {

	double r = annual_interest_rate / 100 / 12;
	int n = years * 12;

	return (principal_amount * r * pow(1 + r, n) / (pow(1 + r, n) - 1));
}

/**
 * Determine the total payment of loan given mortgage princile, annual interest rate (%), and mortgage years.
 *
 * @param principal_amount - float type.
 * @param annual_interest_rate - value of parcentage rate, e.g. 5 means 5%, float type.
 * @param years - number of mortgage year, int type.
 * @return - the total payment of the loan, float type.
 */
float total_payment(float principal_amount, float annual_interest_rate,
		int years) {

	return (principal_amount
			+ total_interest(principal_amount, annual_interest_rate, years));

}

/**
 * Determine the total interested payed for the loan given mortgage princile, annual interest rate (%), and mortgage years.
 *
 * @param principal_amount - float type.
 * @param annual_interest_rate - value of parcentage rate, e.g. 5 means 5%, float type.
 * @param years - number of mortgage year, int type.
 * @return - the total interest payed by the end of paying off the loan, float type.
 */
float total_interest(float principal_amount, float annual_interest_rate,
		int years) {

	float payment = monthly_payment(principal_amount, annual_interest_rate,
			years);
	return ((payment * years * 12) - principal_amount);

}
