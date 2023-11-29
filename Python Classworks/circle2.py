from math import pi
radius = int(input("Enter the radius: "))
while radius < 0:
    print("Error: radius must be positive.")
    radius = int(input("Enter the radius: "))
else:
    area = pi * radius * radius
    print("The area of the circle is", area)
    print(f"The area of the circle is {area:.2f}")