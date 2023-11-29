# -*- coding: utf-8 -*-
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))

if y != 0:
    print("The result is", x/y)
else:
    print("Error. Dividing by zero is not allowed.")
    print("Enter a valid second number.")
