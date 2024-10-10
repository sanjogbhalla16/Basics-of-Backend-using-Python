class Car:
    # constructor
    total_car = 0

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol and Diesel"

    @staticmethod
    def general_description():
        return "Cars are a means of transport"

    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # taken this from the above class
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla_car = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla_car, Car))
# print(isinstance(my_tesla_car, ElectricCar))
# print(my_tesla_car.battery_size)
# print(my_tesla_car.full_name()) # this will show an error saying object has no attribute 'brand'
# print(my_tesla_car.get_brand())

# print(my_tesla_car.fuel_type())


# my_car = Car("Toyota", "Corolla")

# test1 = Car("Tata", "Nexon")
# test2 = Car("Tata", "Punch")
# print(test1.general_description())  # this will give an error as
# print(Car.general_description())

# my_car = Car("Toyota", "Corolla")
# print(my_car.__brand)
# print(my_car.model)
# print(my_car.full_name())


class Battery:
    def battery_info(self):
        return "this is Battery"


class Engine:
    def engine_info(self):
        return "this is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
