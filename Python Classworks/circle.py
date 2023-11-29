from math import pi
radius = int(input("Enter the radius: "))
if radius > 0:
    area = pi * radius * radius
    print("The area of the circle is", area)
    print(f"The area of the circle is {area:.2f}")
else:
    print("Error: The radius cannot be negative!")