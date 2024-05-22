# Just highlights how to use basic class __init__ method in python to get started
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("The car " + self.make + " is driving..")

    def stop(self):
        print("The car " + self.make + " is stopping..")


Car_1 = Car("Honda", "City", 2020)
Car_2 = Car("Mahindra", "XUV7OO", 2017)
Car_2.drive()
