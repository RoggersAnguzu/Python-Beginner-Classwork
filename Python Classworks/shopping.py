f = open('shopping.txt', 'r')
total = 0

for line in f:
    item, price, quantity = line.split()
    price = int(price)
    quantity = int(quantity)
    total = total + price * quantity
    
print("Your shopping will cost", total)

f.close()
f = open("shopping.txt", 'r')
print("Item  Price  Quantity")
for line in f:
    print(line[:-1])

    
