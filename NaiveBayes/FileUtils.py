from Car import Car


def read_cars(path):
    cars = []
    for line in open(path):
        args = line.split(',')
        if len(args) < 7:
            raise Exception("Invalid file!")
        else:
            car = Car(args[0], args[1], args[2], args[3], args[4], args[5], args[6].rstrip())
            cars.append(car)
    return cars

