class Perceptron:
    NUMBER_OF_LETTERS = 26

    def __init__(self):
        self.weights = [0] * self.NUMBER_OF_LETTERS
        self.threshold = 1

    def net(self, input_x):
        self.check_arg(input_x)
        val = 0
        for w, x in zip(self.weights, input_x):
            val += w * x
        return val

    def output(self, input_x):
        self.check_arg(input_x)
        return self.net(input_x) >= self.threshold

    def train(self, output, desired_output, learning_parameter, input_x):
        self.check_arg(input_x)

        desired_minus_output = desired_output - output
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + desired_minus_output * learning_parameter * input_x[i]
        self.threshold = self.threshold + desired_minus_output * learning_parameter

    # exceptions

    def check_arg(self, input_x):
        if len(input_x) != self.NUMBER_OF_LETTERS:
            raise ValueError("Number of weights (letters) doesn't correspond to length of input array")
