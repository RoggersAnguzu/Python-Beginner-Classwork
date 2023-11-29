gradebook = {}
for i in range(5):
    name = input("Name of student: ")
    score = float(input("Score of student: "))
    gradebook[name] = score
    

print('STUDENTS:')
for item in list(gradebook.keys()):
    print(item)
print('GRADES')
for key in gradebook:
    print(key, gradebook[key])