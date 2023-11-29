receipt = float(input("Firt receipt or -1 to quit: "))
total = 0

while receipt != -1: # -1 is the sentinel
    total = total + receipt
    receipt = float(input("Next receipt or -1 to quit: "))
    
print("Your total for the day is", total)
