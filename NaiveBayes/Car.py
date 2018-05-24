import Enums


class Car:
    def __init__(self, buying_price, maintenance_price, doors, capacity, boot_size, safety, car_class):
        self.buying_price = Enums.Price(buying_price)
        self.maintenance_price = Enums.Price(maintenance_price)
        self.doors = Enums.Doors(doors)
        self.capacity = Enums.Capacity(capacity)
        self.boot_size = Enums.BootSize(boot_size)
        self.safety = Enums.Safety(safety)
        self.car_class = Enums.CarClass(car_class)
