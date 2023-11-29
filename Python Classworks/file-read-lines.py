filename = "../files2/mystory.txt"
#filename = input("Enter the file name: ")
f = open(filename, 'r')
for line in f:
    print(line[:-1])