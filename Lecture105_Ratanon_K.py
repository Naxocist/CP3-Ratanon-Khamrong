class Vehicle:
    serialCode = ""
    licenseCode = ""

    def turnonAirconditionor(self):
        print("Turn on : Air")

    def showlicensecode(self):
        print(self.licenseCode)


class Pickup(Vehicle):
    pass


class Car(Vehicle):
    pass


class Estatecar(Vehicle):
    pass


class Van(Vehicle):
    pass


pickup = Pickup()
pickup.turnonAirconditionor()
car = Car()
car.turnonAirconditionor()
estatecar = Estatecar()
estatecar.turnonAirconditionor()
van = Van()
van.turnonAirconditionor()
