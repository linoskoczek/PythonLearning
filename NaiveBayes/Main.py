import FileUtils
from Car import Car
from NaiveBayes import NaiveBayes

test_set = FileUtils.read_cars('car_bayes/test')
training_set = FileUtils.read_cars('car_bayes/training')

nb = NaiveBayes(training_set, test_set)

nb.loop_test_set()

userInput = input('Enter your input or type q to exit:')
while userInput != 'q':
    inp = userInput.split(',')
    car = Car(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6])
    test_set = [car]
    nb = NaiveBayes(training_set, test_set)
    nb.loop_test_set()
    userInput = input('Enter your input or type q to exit:')
