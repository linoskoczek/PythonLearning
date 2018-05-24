from fractions import Fraction
from Enums import Safety, CarClass


class NaiveBayes:

    def __init__(self, training_cars, test_cars):
        self.training_cars = training_cars
        self.test_cars = test_cars
        self.number_of_different_classes = self.num_of_classes()
        self.temp_smaller_set = None

    def num_of_classes(self):
        classes = set()
        for car in self.training_cars:
            classes.add(car.car_class)
        return len(classes)

    def loop_test_set(self):
        for car in self.test_cars:
            self.naive_bayes(car)

    def naive_bayes(self, car):
        probabilities = {}
        for single_class in CarClass:
            self.set_temp_set_to_cars_with_class(single_class)
            probabilities[single_class] = self.probability(car.buying_price, car.maintenance_price, car.doors, car.capacity, car.boot_size, car.safety)
        print(probabilities)

        guessed = max(probabilities, key=probabilities.get)
        actual = car.car_class
        if guessed == actual:
            print("[+]", end=' ')
        else:
            print("[-]", end=' ')
        print('{0:8s} {1:20s} {2:7s} {3:10s}'.format("Guessed:", guessed, "Actual:", actual))

    def set_temp_set_to_cars_with_class(self, car_class):
        self.temp_smaller_set = []
        for car in self.training_cars:
            if car.car_class == car_class:
                self.temp_smaller_set.append(car)

    def probability_class(self):
        numerator = len(self.temp_smaller_set) + 1
        denominator = len(self.training_cars) + self.number_of_different_classes
        return Fraction(numerator, denominator)

    def probability_buying_price(self, arg):
        numerator = 1
        buying_prices = set()

        for car in self.temp_smaller_set:
            if car.buying_price == arg:
                numerator += 1

        for car in self.training_cars:
            buying_prices.add(car.buying_price)

        denominator = len(self.temp_smaller_set) + len(buying_prices)
        return Fraction(numerator, denominator)

    def probability_maintenance_price(self, arg):
        numerator = 1
        maintenance_prices = set()

        for car in self.temp_smaller_set:
            if car.maintenance_price == arg:
                numerator += 1

        for car in self.training_cars:
            maintenance_prices.add(car.maintenance_price)

        denominator = len(self.temp_smaller_set) + len(maintenance_prices)
        return Fraction(numerator, denominator)

    def probability_doors(self, arg):
        numerator = 1
        doors = set()

        for car in self.temp_smaller_set:
            if car.doors == arg:
                numerator += 1

        for car in self.training_cars:
            doors.add(car.doors)

        denominator = len(self.temp_smaller_set) + len(doors)
        return Fraction(numerator, denominator)

    def probability_capacity(self, arg):
        numerator = 1
        capacities = set()

        for car in self.training_cars:
            capacities.add(car.capacity)

        for car in self.temp_smaller_set:
            if car.capacity == arg:
                numerator += 1

        denominator = len(self.temp_smaller_set) + len(capacities)
        return Fraction(numerator, denominator)

    def probability_boot_size(self, arg):
        numerator = 1
        boot_sizes = set()

        for car in self.training_cars:
            boot_sizes.add(car.boot_size)

        for car in self.temp_smaller_set:
            if car.boot_size == arg:
                numerator += 1

        denominator = len(self.temp_smaller_set) + len(boot_sizes)
        return Fraction(numerator, denominator)

    def probability_safety(self, arg):
        numerator = 1
        safeties = set()

        for car in self.temp_smaller_set:
            if car.safety == arg:
                numerator += 1

        for car in self.training_cars:
            safeties.add(car.safety)

        denominator = len(self.temp_smaller_set) + len(safeties)
        return Fraction(numerator, denominator)

    def probability(self, buying_price, maintenance_price, doors, capacity, boot_size, safety):

        number = 1
        number *= self.probability_buying_price(buying_price)
        number *= self.probability_maintenance_price(maintenance_price)
        number *= self.probability_doors(doors)
        number *= self.probability_capacity(capacity)
        number *= self.probability_boot_size(boot_size)
        number *= self.probability_safety(safety)
        number *= self.probability_class()
        return float(number)

