class Vehicle:
    def drive(self):
        print("Generic vehicle is being driven.")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle is being pedaled.")

vehicle = Vehicle()
vehicle.drive()  

car = Car()
car.drive()  

bicycle = Bicycle()
bicycle.drive()  
