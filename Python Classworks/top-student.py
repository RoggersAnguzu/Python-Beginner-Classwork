f = open('grades.txt', 'r')
topstudent = 'Nobody'
topgrade = 0
for line in f:
    name, grade = line.split()
    grade  = int(grade)
    if grade > topgrade:
        topgrade = grade
        topstudent = name

print("The top student is", topstudent)
print("Their grade is", topgrade)

    
