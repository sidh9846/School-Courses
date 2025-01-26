/*
 -------------------------------------
 File:    myword.c
 Project: a3
 file description
 -------------------------------------
 Author:  Manveer Sidhu
 ID:      169029846
 Email:   sidh9846@mylaurier.ca
 Version  2024-02-02
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include "myword.h"

#define MAX_LINE_LEN 1000
#define MAX_WORDS 1000

// You can copy here the functions in mysttring.c if you want to use them in the
// following functions. You can also add other auxiliary functions here.

/**
 * Load word data from file, and insert words a directory represented by char array.
 *
 * @param  FILE *fp -   file pointer to an opened text file
 * @param *dictionary - char pointer to a char array where dictionary words are stored.
 *                      It's up to your design on how to store words in the char array.
 * @return - the number of words added into the dictionary.
 */
int create_dictionary(FILE *fp, char *dictionary) {
// your code

	char line[1000];
	char delimiters[] = " .,\n\t\r";
	char *token;
	int count = 0;
	while (fgets(line, 1000, fp) != NULL) {
		token = (char*) strtok(line, delimiters);
		while (token != NULL) {
			count++;
			strcat(dictionary, token);
			strcat(dictionary, ",");
			token = (char*) strtok(NULL, delimiters);
		}
	}
	return count;
}

/**
 * Determine if a given word is contained in the given dictionary.
 *
 * @param *dictionary -  char pointer to a char array of given dictionary.
 * @param *word  -  pointer to a given word.
 *
 * @return - TRUE if the word is in the dictionary, FALSE otherwise.
 */
BOOLEAN contain_word(char *dictionary, char *word) {
// your code

	BOOLEAN contains = FALSE;

	if (word == NULL || *word == '\0') {
		return contains;
	} else {
		char temp[20] = { 0 };
		strcat(temp, ",");
		strcat(temp, word);
		strcat(temp, ",");

		if (strstr(dictionary, temp) != NULL) {
			contains = TRUE;
		}
	}
	return contains;
}

/**
 * Process text data from a file for word statistic information of line count, word count, keyword count, and frequency of keyword.
 *
 * @param *fp -  FILE pointer of input text data file. .
 * @param *words  -  WORD array for keywords and their frequencies.
 * @param *dictionary  -  stop-word/common-word dictionary.
 *
 * @return - WORDSTATS value of processed word stats information.
 */
WORDSTATS process_words(FILE *fp, WORD *words, char *dictionary) {
// your code

	char line[MAX_LINE_LEN];
	char delimiters[] = " .,\n\t\r";
	char *word_token;
	WORDSTATS ws = { 0, 0, 0 };

	while (fgets(line, MAX_LINE_LEN, fp) != NULL) {

		ws.line_count++;

		for (int j = 0; line[j] != 0; j++) {
			if ((65 <= line[j] && line[j] <= 90)) {
				line[j] += 32;
			}
		}

		word_token = (char*) strtok(line, delimiters);

		while (word_token != NULL) {

			ws.word_count++;

			if (contain_word(dictionary, word_token) == FALSE) {
				int i = 0;

				while ((i < ws.keyword_count)
						&& (strcmp(word_token, words[i].word) != 0)) {
					i++;
				}

				if (i < ws.keyword_count) {
					words[i].count++;
				} else {
					strcpy(words[i].word, word_token);
					words[i].count = 1;
					ws.keyword_count++;
				}
			}
			word_token = (char*) strtok(NULL, delimiters);
		}
	}
	return ws;
}

