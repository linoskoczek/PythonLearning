import math
import os
import random

import Settings


class Perceptron:

    def __init__(self, training_dir):
        self.weights = [random.random() for _ in range(Settings.NUMBER_OF_LETTERS)]
        self.normalize_weights()
        self.threshold = 1
        self.training_dir = training_dir
        self.name = os.path.basename(training_dir)
        print("created perceptron for", self.name)

    def net(self, input_x):
        self.check_arg(input_x)
        val = 0
        for w, x in zip(self.weights, input_x):
            val += w * x
        return val - self.threshold

    def output(self, input_x):
        self.check_arg(input_x)
        return self.activation_function(input_x)

    def desired_output(self, language):
        desired_value = 0
        if language == self.name:
            desired_value = 1
        return desired_value

    def train(self, input_x, language):
        desired_value = self.desired_output(language)
        output = self.output(input_x)
        # print('willing to have', desired_value)
        # print('before:', output)
        self.update_weights(output, desired_value, Settings.LEARNING_PARAMETER, input_x)
        # print('after:', self.output(input_x))
        return output

    def update_weights(self, output, desired_output, learning_parameter, input_x):
        self.check_arg(input_x)

        coefficient = learning_parameter * (desired_output - output) * output * (1 - output)
        for i in range(len(self.weights)):
            self.weights[i] += coefficient * input_x[i]

        self.threshold -= coefficient
        # self.normalize_weights()

    def normalize_weights(self):
        vector_length = 0
        for w in self.weights:
            vector_length += w * w
        vector_length = vector_length ** 0.5

        for i in range(len(self.weights)):
            self.weights[i] /= vector_length

    def activation_function(self, input_x):  # unipolar sigmoid
        return 1 / (1 + math.exp(-self.net(input_x)))

    # exceptions

    def check_arg(self, input_x):
        if len(input_x) != Settings.NUMBER_OF_LETTERS:
            raise ValueError("Number of weights (letters) doesn't correspond to length of input array")
