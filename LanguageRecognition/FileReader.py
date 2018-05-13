import os

import Settings


class FileReader:
    def __init__(self, path):
        self.file = path

    def get_letter_values(self):
        letters = [0] * Settings.NUMBER_OF_LETTERS
        txt_file = open(self.file)
        letter_count = 0
        for line in txt_file:
            for letter in line:
                letter = letter.lower()
                letter_no = ord(letter) - 97
                if 0 <= letter_no <= 25:  # not compatible with special letters
                    letters[letter_no] += 1
                    letter_count += 1

        if letter_count == 0:
            print("ERROR: Empty file given as a training set!")
        else:
            for i in range(len(letters)):
                letters[i] /= letter_count

        return letters

    def get_language_name(self):
        return os.path.basename(self.file)[:2]
