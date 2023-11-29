fname = input("Enter the file name: ")
f = open(fname, 'w')

f.write("Item\t\t\tQuantity\n")
while True:
    item = input("Enter the item: ")
    if item == '':
        break
    else:
        quantity = input("Enter the quantity: ")
        f.write(item + "\t\t\t" + str(quantity) + '\n')
f.close()