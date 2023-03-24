# Create a Vehicle class which has the following instance attributes: color(string),
# type_of_vehicle(string), year_of_market_release(int) and the following class attributes:
# wheels(int) , no_of_doors(int) and the following methods: changeColor, describeVehicle(print
# all the attributes), brakeCar(print the attributes along with “braking”) and startCar (print the
# attributes along with “starting”)

class Vehicle:
    wheels = 4
    no_of_doors = 4

    def __init__(self, color, type, relaseyear):
        self.color = color
        self.type = type
        self.relaseyear = relaseyear

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return "color changed"

    def describe_vehical(self):
        print("The color of vehicle is", self.color, 'the type is ', self.type, 'relased year is ', self.relaseyear)

    def breake_car(self):
        print(self.describe_vehical(), "breaking")

    def star_car(self):
        print("starting")


def main():
    v1 = Vehicle("black", "mercedes", 1970)
    v1.describe_vehical()
    v2 = Vehicle("red", "Audi", 1980)
    v2.describe_vehical()
    print(v1.set_color("blue"))
    print(v1.describe_vehical())
    print(v2.star_car())
    print(v1.breake_car())


if __name__ == '__main__':
    main()
