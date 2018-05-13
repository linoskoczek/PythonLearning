import glob
import os

import Settings
from FileReader import FileReader
from Perceptron import Perceptron


class Layer:
    def __init__(self):
        self.perceptrons = []
        languages = self.detect_languages()
        self.create_perceptrons(languages)
        self.train_perceptrons()

    def detect_languages(self):
        return [d for d in os.listdir(Settings.TRAINING_DIR)]

    def create_perceptrons(self, languages):
        for lang in languages:
            self.perceptrons.append(
                Perceptron(os.path.basename(lang))
            )

    def train_perceptrons(self):
        files = glob.glob(Settings.TRAINING_DIR + '/**/*.txt', recursive=True)
        repeat = 1
        while repeat == 1:
            repeat = 0

            for f in files:
                error = 0
                reader = FileReader(f)
                letter_values = reader.get_letter_values()
                lang = reader.get_language_name()

                for p in self.perceptrons:
                    output = p.train(letter_values, lang)
                    error += 0.5 * (p.desired_output(lang) - output) ** 2
                if error > Settings.MAX_ERROR:
                    repeat = 1

    def test_output(self, input_file):
        reader = FileReader(input_file)
        letter_values = reader.get_letter_values()

        values = {}
        for p in self.perceptrons:
            values[p.name] = p.output(letter_values)

        print(values)

        return max(values, key=values.get)

