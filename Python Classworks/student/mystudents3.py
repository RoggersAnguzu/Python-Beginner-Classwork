from student import Student
student_list = []
name = " "

def getStuInfo():
    while True:
        name = input("Name: ")
        if name == "":
            return null
        idnum = input("ID: ")
        year = int(input("Year: "))
        return Student(name, idnum, year)
    
stdunts_list