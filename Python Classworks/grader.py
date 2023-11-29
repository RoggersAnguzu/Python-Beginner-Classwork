"""
This program calculates letter grade
given the numeric score
"""
score = int(input("Enter the numeric score: "))
if score < 0:
    print("Score must be 0 or higher!")
elif score > 100:
    print("Score must be 100 or lower!")
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print("The grade is", grade)