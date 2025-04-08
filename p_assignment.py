# Base class: Vehicle
class Vehicle:
    def move(self):
        """Generic move method for vehicles"""
        pass  # To be overridden by subclasses

# Derived class: Car
class Car(Vehicle):
    def move(self):
        """Car-specific move method"""
        print("Driving 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        """Plane-specific move method"""
        print("Flying ✈️")

# Derived class: Dog (to show polymorphism across animals as well)
class Dog(Vehicle):
    def move(self):
        """Dog-specific move method"""
        print("Running 🐕")

# Create objects of each class
car = Car()
plane = Plane()
dog = Dog()

# Call the move method on each object
car.move()  
plane.move() 
dog.move()  
