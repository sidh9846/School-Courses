/*
 -------------------------------------
 File:    myrecord.c
 Project: a4
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-09
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "myrecord.h"
#include "mysort.h"

/*
 * Convert a percentage grade to letter grade defined by percentage ranges
 * A+=[90, 100], A=[85, 90), A-=[80, 85), B+=[77, 80), B=[73, 77) B=[70, 73),
 * C+=[67, 70), C=[63, 77), C-=[60, 63), D+=[57,60),D=[53,57),D=[50,53), F=[0,50).
 *
 * @param score -  percetage grade.
 *
 * @return - letter grade wrapped in GRADE structure type.
 */
GRADE grade(float score) {
	GRADE r = { "F" };
// your code

	if (score >= 90) {
		strcpy(r.letter_grade, "A+");
	} else if (score >= 85) {
		strcpy(r.letter_grade, "A");
	} else if (score >= 80) {
		strcpy(r.letter_grade, "A-");
	} else if (score >= 77) {
		strcpy(r.letter_grade, "B+");
	} else if (score >= 73) {
		strcpy(r.letter_grade, "B");
	} else if (score >= 70) {
		strcpy(r.letter_grade, "B-");
	} else if (score >= 67) {
		strcpy(r.letter_grade, "C+");
	} else if (score >= 63) {
		strcpy(r.letter_grade, "C");
	} else if (score >= 60) {
		strcpy(r.letter_grade, "C-");
	} else if (score >= 57) {
		strcpy(r.letter_grade, "D+");
	} else if (score >= 53) {
		strcpy(r.letter_grade, "D");
	} else if (score >= 50) {
		strcpy(r.letter_grade, "D-");
	}

	return r;
}

/*
 *  Take the RECORD data array as input, compute the average score, standard deviation,
 *  median of the score values of the record data, and returns the results in STATS type.
 *
 *  @param dataset -  input record data array.
 *  @param count -  the number of data record in dataset array.
 *  @return  -  stats value in STATS type.
 */
STATS process_data(RECORD *dataset, int count) {
// your code

// var def
	STATS stats = { 0 };
	int total = 0;
	int mean = 0;
	float diff = 0;
	float mean_sqr = 0;
	float stddev = 0;
	int median = 0;
	float *a[count];

	// compute mean
	for (int i = 0; i < count; i++) {
		total += dataset[i].score;
		a[i] = &(dataset[i].score);
	}
	mean = total / count;

	// compute stddev
	mean_sqr = pow(mean, 2);

	for (int i = 0; i < count; i++) {
		diff += pow(dataset[i].score, 2) - mean_sqr;
	}

	stddev = sqrt((1 / (float) count) * diff);

	// compute median
	quick_sort_inc(a, 0, count - 1);

	if (count % 2 == 0) {
		median = (*a[(count / 2) - 1] + *a[count / 2]) / 2;
	} else {
		median = *a[count / 2];
	}

	// set values
	stats.count = count;
	stats.mean = mean;
	stats.stddev = stddev;
	stats.median = median;

	return stats;
}

/*
 *  Import record data from file and retrieves and stores all record entries
 *  in the RECORD array passed by records, and returns the number of record count.
 *
 *  @param *fp -  FILE pointer to intput file.
 *  @param dataset - array of RECODR type to store record data.
 *  @return   - number record count
 */
int import_data(FILE *fp, RECORD *dataset) {
// your code
	char delimiters[] = " ,\n\r";
	char line[100];
	int i = 0; // record counter char *token = NULL;
	while (fgets(line, sizeof(line), fp) != NULL) {
		sscanf(line, "%[^, ],%f", dataset[i].name, &dataset[i].score);
		i++;
	}
	return i;
}

/*
 *  This function takes output file named outfilename,
 *  RECORD array by records,and output stats information,
 *   and processed record data to files in required format.
 *
 *  @param *fp -  FILE pointer to output file.
 *  @param count -  the number of data record in dataset array.
 *  @return - returns 1 if successful; 0 if count < 1
 */
int report_data(FILE *fp, RECORD *dataset, int count) {
// your code

	char *name;
	float score;
	GRADE letter;

	for (int i = 0; i < count; i++) {
		name = dataset[i].name;
		score = dataset[i].score;
		letter = grade(score);

		fprintf(fp, "%s,%.1f,%s\n", name, score, letter.letter_grade);
	}
	return 1;

}
