total = 0
count = 0

while True:
    score = float(input("Current score or a -ve num to quit: "))
    if score < 0:
        break
    total = total + score
    count = count + 1
    
if count != 0:
    print("The average score is", total/count)
else:
    print("You did not enter any scores.")
