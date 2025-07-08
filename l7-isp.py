# ISP(Interface Segregation Principle) - Clients should not be forced to depend on interfaces
# they do not use. Meaning, a class should not be required to implement methods it doesn't need.


"""

Code Violating LSP

"""


class Machine:
    def rotate_motor(self):
        print("motor rotating")

    def blow_air(self):
        print("air blowing")

    def heat_water(self):
        print("water heating")


class Fan(Machine):
    def heat_water(self):
        raise Exception("Fan can't heat water")


class WashingMachine(Machine):
    def blow_air(self):
        raise Exception("Washing Machine can't blow air")


"""

ISP Compliant code

"""


class Motor:
    def rotate_motor(self):
        print("motor rotating")


class Blower:
    def blow_air(self):
        print("air blowing")


class Heater:
    def heat_water(self):
        print("water heating")


class Fan(Motor, Blower):
    pass


class WashingMachine(Motor, Heater):
    pass
