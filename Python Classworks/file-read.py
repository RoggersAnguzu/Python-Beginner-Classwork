#filename = "mystory.txt"
filename = input("Enter the file name: ")
f = open(filename, 'r')
mystory = f.read()
f.close()
print(mystory)