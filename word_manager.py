import csv
import random
from datetime import datetime

# Intervals in days for reviewing new words
INTERVALS = [1, 3, 7, 10, 15, 30, 60, 90]


class WordManager:
    """
    Class for managing words from a CSV file.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.load_words_from_csv()
        self.words_to_review = []

    def load_words_from_csv(self):
        """
        Load words from CSV file.
        :return: List of tuples containing date added, Spanish word, and Czech translation
        """
        words = []
        invalid_count = 0

        try:
            with open(self.file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) != 3:
                        print(f"Skipping row due to incorrect column count: {row}")
                        continue

                    try:
                        date_added = datetime.strptime(row[0], '%Y-%m-%d')
                        spanish_word = row[1]
                        czech_translation = row[2]
                        words.append((date_added, spanish_word, czech_translation))
                    except ValueError:
                        print(f"Invalid date: {row[0]}")
                        invalid_count += 1

            if invalid_count > 0:
                print(f"Number of invalid rows skipped: {invalid_count}")

            return words

        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return []

    def check_words_for_review(self):
        """
        Check words for review based on the defined intervals.
        """
        today = datetime.now()
        self.words_to_review.clear()

        for date_added, spanish_word, czech_translation in self.words:
            days_since_added = (today - date_added).days
            if days_since_added in INTERVALS:
                self.words_to_review.append((spanish_word, czech_translation))

        # Shuffle the words to review
        self.words_to_review = self.get_random_words(len(self.words_to_review))

    def get_random_words(self, count=50):
        """
        Get random words for review.
        :param count: Number of words to return
        :return: List of random words for review
        """
        random.shuffle(self.words_to_review)
        return self.words_to_review[:count]

    def get_next_batch(self, start_index, batch_size=50):
        """
        Get a batch of words to review.
        :param start_index: Index to start from
        :param batch_size: Number of words to fetch
        :return: List of words for the specified batch
        """
        end_index = start_index + batch_size
        return self.words_to_review[start_index:end_index]