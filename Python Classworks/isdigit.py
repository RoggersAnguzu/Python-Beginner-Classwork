number = input("How many item? ")
if number.isdigit():
    number = int(number)
    print("You have", number, 'items.')
else:
    print("You have", number, 'items.')