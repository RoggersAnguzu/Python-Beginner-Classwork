from math import pi

radius = float(input("Enter the radius: "))

def checkinput(x):
    if x > 0:
        return x
    else:
        return -1 # A code meaning input has problem
if checkinput(radius) > 0:
    area = pi * radius * radius
    print("The area of the circle is", area)