score = input("Next score or <ENTER> to quit: ")
total = 0
count = 0

while score != "":
    score = float(score)
    total = total + score
    count = count + 1
    score = input("Next score or <ENTER> to quit: ")
    
if count != 0:
    print("The average score is", total/count)
else:
    print("You have not entered any scores.")
    
