from math import sqrt
x = float(input("Enter a number: "))
tolerance = 0.01
guess = x / 2
count = 0
while abs(guess * guess - x) > tolerance:
    guess = (guess + x/guess)/2
    count = count + 1
    
print(guess)
print(sqrt(x))
print(count)