total = 0
count = 0

while True:
    score = input("Current score or <ENTER> to quit: ")
    if score == "":
        break
    score = float(score)
    total = total + score
    count = count + 1
    
if count != 0:
    print("The average score is", total/count)
else:
    print("You did not enter any scores.")
