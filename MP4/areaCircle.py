# Name: Dana Huang
# School: FEU Alabang
# Machine Problem number - 2

import math

class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.rad = radius

    def Area(self):
        ans = Circle.pi * pow(self.rad, 2)
        print("The area is: {:.2f}".format(ans))

    def Perimeter(self):
        ans = 2 * Circle.pi * self.rad
        print("The perimeter is: {:.2f}".format(ans))

# functions
def PositiveCheck(rad):
    print("You have entered a negative value. Please enter a positive integer\n")
    input_r = input("Enter radius: ")
    temp_r = float(input_r)
    rad = int(float(input_r))
    return rad, temp_r

def FloatCheck(rad):
    print("You have entered a float. Please enter a positive whole number\n")
    input_r = input("Enter radius: ")
    temp_r = float(input_r)
    rad = int(float(input_r))
    return rad, temp_r

def checker(rad, temp_r):
    if rad < 0:
        while rad < 0:
            rad, temp_r = PositiveCheck(rad)
            if rad != temp_r:
                while rad != temp_r:
                    rad, temp_r = FloatCheck(rad)
                    if rad == temp_r:
                        return rad
                        break
            elif rad > 0:
                return rad
                break
    elif rad != temp_r:
        while rad != temp_r:
            rad, temp_r = FloatCheck(rad)
            if rad < 0:
                while rad < 0:
                    rad, temp_r = PositiveCheck(rad)
                    if rad > 0:
                        return rad
                        break
            elif rad == temp_r:
                return rad
                break
    else:
        return rad

input_r = input("Enter radius: ")
temp_r = float(input_r)
rad = int(float(input_r))


rad = checker(rad, temp_r)

test = Circle(rad)
test.Area()
test.Perimeter()