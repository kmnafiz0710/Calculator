# class Cat:
#     def __init__(self,name):
#         self.name=name


class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

    def bark(self):  # Method
        return f"{self.name} {self.age} says Woof!"


my_dog = Dog("Buddy", 3)  # Creating an object of the Dog class
print(my_dog.bark())      # Calling a method on the object
