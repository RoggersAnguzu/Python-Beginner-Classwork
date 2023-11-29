from math import sqrt

x = float(input("Enter a number: "))
count = int(input("Number of iterations: "))
guess = x/2 # Initial guess

for i in range(count):
    guess = (guess + x / guess)/2

print(f"Our estimate is {guess:.2f}")
print(f"Python's estimate is {sqrt(x):.2f}")