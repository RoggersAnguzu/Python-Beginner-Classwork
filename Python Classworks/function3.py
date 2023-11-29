name = input("What is your name? ")
age = int(input("How old are you? "))

def greet(nm, x):
    print("Hello", nm)
    print("Nice to meet you.")
    print("You don't look a day over", x - 10)
    
greet(name, age)
    