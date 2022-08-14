"""
Object oriented programming
= use of objects, classes
almost everything in python is an object

An object is an instance of a class which has properties and methods.
Class is a blueprint for creating objects
Advantages of an oop:
- help you bundle functionalities together
- easy creation of a class instance (object)
- ability to modify methods of a class without changing the class
- allows you to create a user-defined data structure

Class has methods - functions defined in the mody of the class
first argument in the function is (self)
has attributes - variables defined in a class

__init__() - constructor (donda-donda = underscore-underscore = __ )
Instance variables are for data unique to each instance
Class variables are for attributes and methods shared by all instances of the class
"""
import self as self


class Car:
    def __init__(self, name, num_doors=4, exotic = False): #e. g.name is instance variable
        self.name = name
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in_motion = False
        self.speed = 0

    def doors(self):
        if self.door_no not in [2,3,4]:
            return f"{self.name} has invalid door numbers"
        return self.door_no
    def drive(self):
        self.in_motion = True


    def acceleration(self, acceleration=10):
        if self.in_motion:
            self.speed += acceleration

    def stop(self):
        self.in_motion = False


car1 = Car(name="Toyota Prius", num_doors=4)
car2 = Car(name="Tesla A20", num_doors=2, exotic=True)
print(car1)
car2.drive()
car2.acceleration(30)
print(car1.speed)
print(car2.speed)