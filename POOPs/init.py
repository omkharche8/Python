# Trying out init function features.
class MainClass:
    def __init__(self, name):
        self.name = name
        print(name)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2
        print(self.area)


name_one = MainClass("Om")
name_two = MainClass("Robin")
area_one = Circle(5)
area_two = Circle(7)


#Calling Parents class __init__ in inheritancce

class Master():
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is the Master")

class Slave(Master):
    def __init__(self, name, age):
        super().__init__(name)   #Calling Master __init__ here
        self.age = age
        print(f"Slave with {self.name} and {self.age}")


super_test = Slave("Robin", 20)



