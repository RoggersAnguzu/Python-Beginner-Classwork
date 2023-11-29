from student import Student
student_list = []

while True:
    name = input("Name: ")
    if name == "":
        sure = input("Are you sure, Yes or No? ")
        if sure.lower() == 'yes':
            break
        else:
            name = input("Name: ")
    idnum = input("ID: ")
    year = int(input("Year: "))
    stu = Student(name, idnum, year)
    student_list.append(stu)
    
for item in student_list:
    print(item.getName(), item.getIdnum(), item.getYear())

if len(student_list) > 0:
    print("Number of students:", student_list[0].getCount())
else:
    print("You have not entered any students.")