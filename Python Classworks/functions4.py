def add(a=1, b=10):
    total = 0
    for i in range(a, b+1):
        total = total + i
    return total

# To add numbers from n to m
first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
  
print('The sum is', add(first, last))
    