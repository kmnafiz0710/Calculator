# task 1
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print(f"Brand name of this car: {self.brand}, \n and the color of this car: {self.color}")

my_car = Car("Toyota", "Red")   #instance

my_car.info()

# task 2
class Student:
    def __init__(self,name,grade):
        self.Name=name
        self.Grade=grade

    def info(self):
        print(f"Student Name is {self.Name}  and his grade is {self.Grade}")
student1= Student("Hasan","A+")  #instance
student2= Student("Khaled","A-")   #instance

student1.info()
student2.info()