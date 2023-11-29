filename = "mystory.txt"
f = open(filename, 'r')
while True:
    line = f.readline()
    if line == '':
        break
    print(line, end='')
    
