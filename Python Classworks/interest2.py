"""
This program calculates the interest every year
"""
principal = float(input("Enter the principal: "))
term = int(input("Enter the term: "))
rate = float(input("Enter the interest rate [0-100]: "))
if rate >= 0 and rate <= 100:
    print(f"{'Year':4}  {'Principal':>15}   {'Interest':>13}")
    for i in range(1, term+1):
        interest = rate/100 * principal
        principal = principal + interest
        print(f'{i:4d} {principal:15.2f} {interest:15.2f}')    
else:
    print("Error: rate must be in the range [0-100]")
