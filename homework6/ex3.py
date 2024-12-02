class Vehicle:
    def __init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year):
        self.total_distance_travelled = total_distance_travelled
        self.total_fuel_consumed = total_fuel_consumed
        self.mark = mark
        self.model = model
        self.year = year

    def mileage(self):
        m = self.total_distance_travelled / self.total_fuel_consumed
        return m


class Car(Vehicle):
    def __init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year, gcvwr, curb_weight):
        Vehicle.__init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year)
        self.gcvwr = gcvwr
        self.curb_weight = curb_weight

    def towing_capacity(self):
        c = self.gcvwr / self.curb_weight
        return c

    def __str__(self):
        return "The mileage of the car " + str(self.mark) + " with the model " + str(
            self.model) + " made in the year " + str(self.year) + " is " + str(
            self.mileage()) + " and the towing capacity is " + str(self.towing_capacity())


class Motorcycle(Vehicle):
    def __init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year, curb_weight):
        Vehicle.__init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year)
        self.curb_weight = curb_weight

    def towing_capacity(self):
        c = 0.5 * self.curb_weight
        return c

    def __str__(self):
        return "The mileage of the Motorcycle " + str(self.mark) + " with the model " + str(
            self.model) + " made in the year " + str(self.year) + " is " + str(
            self.mileage()) + " and the towing capacity is " + str(self.towing_capacity())


class Truck(Vehicle):
    def __init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year, gcvwr, curb_weight,
                 passenger_weight, cargo_weight):
        Vehicle.__init__(self, total_distance_travelled, total_fuel_consumed, mark, model, year)
        self.curb_weight = curb_weight
        self.passenger_weight = passenger_weight
        self.cargo_weight = cargo_weight
        self.gcvwr = gcvwr

    def towing_capacity(self):
        c = self.gcvwr - (self.curb_weight + self.passenger_weight + self.cargo_weight)
        return c

    def __str__(self):
        return "The mileage of the Truck " + str(self.mark) + " with the model " + str(
            self.model) + " made in the year " + str(self.year) + " is " + str(
            self.mileage()) + " and the towing capacity is " + str(self.towing_capacity())


car = Car(60000, 5000, "Tesla", "X", "2010", 12000, 7000)
print(car)

motorcycle = Motorcycle(10000, 2000, "Yamaha", "R7", "2009", 150)
print(motorcycle)

truck = Truck(200000, 20000, "Ford", "super", "1900", 35000, 12000, 90, 5000)
print(truck)
