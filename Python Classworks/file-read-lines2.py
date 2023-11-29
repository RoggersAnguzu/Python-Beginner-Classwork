import os
filename = "../files2/mystory.txt"
#filename = input("Enter the file name: ")
if os.path.exists(filename):
    f = open(filename, 'r')
    for line in f:
        print(line, end='')
else:
    print('Error: Check filename spelling.')
    
