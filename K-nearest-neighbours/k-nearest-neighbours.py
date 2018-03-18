from math import sqrt


class Iris:
    """Class used to describe various Iris types"""
    def __init__(self, values, label):
        self.values = values
        self.label = label


def distance(train, test):
    num_of_values = len(train.values) - 1
    dist = 0
    for i in range(0, num_of_values):
        dist += (float(train.values[i]) - float(test.values[i]))**2
    return sqrt(dist)


def replace_biggest(list_of_lists, element):
    curr_max = -1
    max_index = -1
    for i in range(len(list_of_lists)):
        if list_of_lists[i][1] > curr_max:
            curr_max = list_of_lists[i][1]
            max_index = i

    list_of_lists[max_index] = element
    return list_of_lists


def determine_label(closest_neighbours):
    labels = {}
    for neighbour in closest_neighbours:
        flower = neighbour[0]
        if flower.label in labels:
            labels[flower.label] += 1
        else:
            labels[flower.label] = 1
    return max(labels, key=labels.get)


def check_labels(predicted, correct):
    print(predicted, correct)
    if predicted == correct:
        return 1
    else:
        return 0


def knn(k, train_set, test_set):
    closest_neighbours = []
    current_max = -1
    guesses = 0
    for test in test_set:
        for train in train_set:
            dist = distance(train, test)
            if len(closest_neighbours) < k:
                closest_neighbours.append([train, dist])
                if dist > current_max:
                    current_max = dist
            elif dist < current_max:
                replace_biggest(closest_neighbours, [train, dist])
                current_max = dist
        guesses += check_labels(determine_label(closest_neighbours), test.label)
        closest_neighbours = []
    print("Accuracy:", guesses/len(test_set) * 100, '%')


def flowers_to_list(file):
    flowers = []
    with open(file) as f:
        for line in f:
            dat = line.strip().split(",")
            flower = Iris(dat[:3], dat[4])
            flowers.append(flower)
    return flowers


train_flowers = flowers_to_list('iris/train.txt')
test_flowers = flowers_to_list('iris/test.txt')

knn(3, train_flowers, test_flowers)
