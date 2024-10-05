class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print(f"Brand name of this car: {self.brand}, and the color of this car: {self.color}")

my_car = Car("Toyota", "Red")   #instance

my_car.info()
