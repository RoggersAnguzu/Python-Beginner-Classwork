def validate(prompt, lower, upper):
    """Validate input.
    Usage: three arguments
    string, int, int
    """
    number = int(input(prompt))
    while True:
        if lower<=number<=upper:
            return number
        else:
            print("The range is", lower, '-', upper)
            number = int(input(prompt))
            
# The grader program
mark = validate("Enter a mark: ", 0, 100)
if mark >= 90:
    print('A')
elif mark >= 80:
    print('B')
elif mark >= 70:
    print('C')
elif mark >= 60:
    print('D')
else:
    print('F')