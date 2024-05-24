# Create a system to manage different types of vehicles in a transportation company.
# The system should have a base class Vehicle with common attributes and methods, and subclasses for specific types of vehicles like Car, Truck, and Motorcycle.
# Each subclass should override a method to display specific information about the vehicle. Additionally, include a method to calculate the total distance a vehicle can travel based on its fuel capacity and fuel consumption rate.



class Vehicle:
    def info(self, name, make, wheels, doors, year):
        print(name + "\n" + make + "\n" + str(wheels) + "\n" + str(doors) + "\n" + str(year))


    def rangecalc(self, name, fcapacity, fconsumption):
        myrange = fcapacity / fconsumption * 100
        print(f"The range of {name} is {myrange}")


class Car(Vehicle):
    def info(self, name, make, wheels, doors, year, car_type):
        super().info(name, make, wheels, doors, year)
        print("Car Type: " + car_type)


class Motorcycle(Vehicle):
    def info(self, name, make, wheels, doors, year, bike_type):
        super().info(name, make, wheels, doors, year)
        print("Bike Type: " + bike_type)


obj1 = Motorcycle()
obj1.rangecalc("Hero", 10, 20)
obj1.info("XUV7OO", "Mahindra", 4, 5, 2020, "Cruiser")

