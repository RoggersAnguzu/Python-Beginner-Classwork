def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

# for testing the functions by module developer
def main():
    x = 100
    y = 50
    print(add(x, y))
    print(minus(x, y))
    print(multiply(x, y))
    print(divide(x, y))

# execute main() conditionally
# i.e. only when the module is 
# run directly, but not when it
# is imported into another prog
if __name__ == '__main__':
    main()