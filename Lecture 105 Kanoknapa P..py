class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOntheAC(self):
        print("Turn on : AC")

class Car(Vehicle):
    def sayHello(self):
        print("Hello")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOntheAC()
car1.sayHello()

pickUp1 = PickUp()
pickUp1.turnOntheAC()

van1 = Van()
van1.turnOntheAC()

estateCar1 = EstateCar()
estateCar1.turnOntheAC()

