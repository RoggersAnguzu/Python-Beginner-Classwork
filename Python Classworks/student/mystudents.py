from student import Student
slst = []
s1 = Student("Maryam", "abc123", 1)
slst.append(s1)
name = input("Enter the student name: ")
idnum = input("Enter the student's ID number: ")
year = input("Enter the student's year in school: ")
s2 = Student(name, idnum, year)
slst.append(s2)
s3 = Student("Mimi", 'cfr657', 2)
slst.append(s3)
print("Class List")
for item in slst:
    print(item.getName(), item.getIdnum(), item.getYear())

print("The number of students is", s1.getCount())


