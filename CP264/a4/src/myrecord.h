/*
 -------------------------------------
 File:    myrecord.h
 Project: a4
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-09
 -------------------------------------
 */
#ifndef MYRECORD_H_
#define MYRECORD_H_

typedef struct {
	char name[20];
	float score;
} RECORD;

typedef struct {
	int count;
	float mean;
	float stddev;
	float median;
} STATS;

typedef struct {
	char letter_grade[3];
} GRADE;

GRADE grade(float score);

int import_data(FILE *fp, RECORD *dataset);

STATS process_data(RECORD *dataset, int count);

int report_data(FILE *fp, RECORD *dataset, int count);

#endif /* MYRECORD_H_ */
