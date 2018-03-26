import random
import re


class Iris:
    """Class to store a kind of Iris and it's values"""
    flowers = []
    labels = []
    threshold = 0

    def __init__(self, values, label):
        self.values = values
        self.label = label


def add_single_flower(line, flowers):
    dat = line.strip().split(",")
    label = dat[4]
    if label not in Iris.labels:
        Iris.labels.append(label)
        label = len(Iris.labels) - 1
    else:
        label = Iris.labels.index(label)
    new_flower = Iris(dat[:3], label)
    flowers.append(new_flower)
    return new_flower


def flowers_to_list(file):
    with open(file) as f:
        for line in f:
            add_single_flower(line, Iris.flowers)
    return Iris.flowers


def output(input_flower):
    wtx = 0.0
    for w, x in zip(Iris.weights, input_flower.values):
        wtx += w * float(x)
    return wtx >= Iris.threshold


def update_weights_and_threshold(input_flower, desired_out, actual_out):
    multiplier = (desired_out - actual_out) * learning_parameter
    for a in range(len(Iris.weights)):
        Iris.weights[a] += multiplier * float(input_flower.values[a])
    Iris.threshold -= multiplier


def ask_for(text, for_what):
    variable = None
    correct = 0
    if for_what == "example":
        while correct < 1:
            correct = 1
            variable = input(text)
            if variable == "X":
                exit(0)
            elif re.match("(\d+.\d+,){4}Iris-\w+", variable) is None:
                print("Incorrect input!")
                correct = 0
        return variable
    elif for_what == "learning_parameter":
        while correct < 1:
            try:
                correct = 1
                variable = float(input(text))
                if variable >= 1 or variable <= 0:
                    raise ValueError()
            except ValueError:
                correct = 0
                print("Please provide a number between 0 and 1 (exclusive)!")
        return variable
    elif for_what == "iterations":
        while correct < 1:
            try:
                correct = 1
                variable = int(input(text))
            except ValueError:
                correct = 0
                print("Please provide a number!")
        return variable


def user_input_loop():
    print("Type 'X' if you want to exit")
    while 1:
        test_flower = ask_for("Enter your own example: 6.4,3.1,5.5,1.8,Iris-virginica: ", "example")
        flower = add_single_flower(test_flower, Iris.flowers)
        result = output(flower)
        if result == flower.label:
            print("[OK]", Iris.labels[flower.label])
        else:
            print("[ERR] got", Iris.labels[result], "but actual label is", Iris.labels[flower.label])


def learn(input_set):
    for i in range(iterations):
        for flower in input_set:
            guess = output(flower)
            if guess != flower.label:
                update_weights_and_threshold(flower, flower.label, guess)


def test(input_set):
    correct_guesses = 0
    for flower in input_set:
        if output(flower) == flower.label:
            correct_guesses += 1

    print("Accuracy:", correct_guesses/len(test_set) * 100, "%\n")


Iris.weights = [random.random()*3 for r in range(3)]
Iris.threshold = random.randint(0, 3)

learning_parameter = ask_for("Please provide learning parameter (0 < alpha < 1): ", "learning_parameter")
iterations = ask_for("Please provide number of iterations: ", "iterations")

training_set = flowers_to_list("iris_perceptron/training.txt")
test_set = flowers_to_list("iris_perceptron/test.txt")

learn(training_set)
test(test_set)
user_input_loop()
