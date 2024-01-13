class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.number_of_wheels = None

    def printname(self):
        print(self.name)

    def drive(self):
        print("I don't know what I am!")


class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model
        self.number_of_wheels = 4

    def print_model(self):
        print(self.model)

    def drive(self):
        print("vroom vroom!")


class Bike(Vehicle):
    def __init__(self, name, color, has_gear):
        super().__init__(name, color)
        self.has_gear = has_gear
        self.number_of_wheels = 2

    def drive(self):
        print("I am good for earth! beep beep!")


u = Vehicle("Unknown", "Unknown")
u.printname()
u.drive()
print(u.number_of_wheels)
print('----------------')
c = Car("BMW", "Black", "X5")
c.printname()
c.print_model()
c.drive()
print(c.number_of_wheels)
print('----------------')
b = Bike("BMX", "Red", True)
b.printname()
b.drive()
# b.print_model()
print(b.number_of_wheels)
print('----------------')
print(isinstance(c, Vehicle))
print(isinstance(c, Car))
print(isinstance(c, Bike))
print(isinstance(u, Vehicle))
print(isinstance(u, Car))
print(isinstance(u, Bike))
print(isinstance(b, Vehicle))
print(isinstance(b, Car))
print(isinstance(b, Bike))