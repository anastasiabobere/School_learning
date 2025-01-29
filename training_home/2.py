class Car:
    def __init__(self, brand, model, year, price, mileage, condition):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.condition = condition

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}, ${self.price}, {self.mileage} km, {self.condition}"


class Sedan(Car):
    def __init__(self, number_seats, brand, model, year, price, mileage, condition):
        self.number_seats = number_seats
        super().__init__(brand, model, year, price, mileage, condition)

    def __str__(self):
        return f"{super().__str__()}, {self.number_seats} seats"


class SUV(Car):
    def __init__(self, four_wheel, brand, model, year, price, mileage, condition):
        super().__init__(brand, model, year, price, mileage, condition)
        self.four_wheel = "4-wheel" if four_wheel else "not a 4-wheel"

    def __str__(self):
        return f"{super().__str__()}, {self.four_wheel} drive"


class Sport_Car(Car):
    def __init__(self, top_speed, brand, model, year, price, mileage, condition):
        self.top_speed = top_speed
        super().__init__(brand, model, year, price, mileage, condition)

    def __str__(self):
        return f"{super().__str__()}, top speed: {self.top_speed} km/h"


class Dealership:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.total_value = 0

    def add_car(self, car):
        self.cars.append(car)

    def calculate_total_value(self):
        self.total_value = sum(car.price for car in self.cars)
        return self.total_value

    def is_high_end(self):
        for car in self.cars:
            if isinstance(car, Sport_Car) and car.price > 70000:
                return 'high-end'
        return 'not high-end'

    def is_family_friendly(self):
        sedans_count = len([car for car in self.cars if isinstance(car, Sedan)])
        suvs_count = len([car for car in self.cars if isinstance(car, SUV)])
        if sedans_count > 3 and suvs_count > 2:
            return 'family-friendly'
        else:
            return 'not family-friendly'

    def __str__(self):
        cars_str = "\n".join(str(car) for car in self.cars)
        return f"Dealership: {self.name}\nCars:\n{cars_str}##################\nTotal value: ${self.total_value}\n Dealership is {self.is_high_end()}\n Dealership is {self.is_family_friendly()}" 


sedans = [
    Sedan(5, "Toyota", "Corolla", 2018, 20000, 10000, "new"),
    Sedan(5, "Toyota", "Camry", 2018, 25000, 15000, "old"),
    Sedan(6, "Toyota", "Yaris", 2018, 15000, 5000, "new"),
    Sedan(5, "Toyota", "Kowow", 2001, 16000, 1000, "old")
]
suv = [
    SUV(True, "Toyota", "Rav4", 2018, 30000, 20000, "new"),
    SUV(False, "Toyota", "Land Cruiser", 2018, 50000, 25000, "old"),
    SUV(True, "Toyota", "Fortuner", 2018, 40000, 15000, "new"),
    SUV(False, "Toyota", "Prado", 2001, 45000, 10000, "old")
]
sport_cars = [
    Sport_Car(200, "Toyota", "Supra", 2018, 600000, 20000, "new"),
    Sport_Car(250, "Toyota", "86", 2018, 500000, 15000, "old"),
]
d1 = Dealership("Toyota Dealership")
d1.add_car(sedans[0])
d1.add_car(sport_cars[0])
d1.add_car(suv[0])
d1.calculate_total_value()

print(d1)
d2 = Dealership("Mercedes Dealership")
d2.add_car(sedans[0])
d2.add_car(sport_cars[1])
d2.add_car(sport_cars[0])
d2.add_car(suv[0])
d2.add_car(suv[3])
d2.calculate_total_value()

print(d2)