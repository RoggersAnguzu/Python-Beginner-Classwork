from car import Car
mycar = Car("Tesla", "Model 3", "Black", 2020)
yourcar = Car("Toyota", "Vitz", "Blue", 2010)

print(mycar)
print()
print(yourcar)
mycar.setColor('White')
print()
print(mycar)
print()
print("We have", mycar.getCount(), 'cars.')
print()

temp = yourcar
yourcar = mycar
mycar = temp

print(mycar)
print()
print(yourcar)