from math import sqrt

x = float(input("Enter a number: "))
count = int(input("Number of iterations: "))
guess = x/2 # Initial guess

i = 0
while i <= count:
    guess = (guess + x / guess)/2
    i = i + 1 # i += 1

print(f"Our estimate is {guess:.2f}")
print(f"Python's estimate is {sqrt(x):.2f}")