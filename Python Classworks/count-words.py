f = open('mystory.txt', 'r')
count = 0
for line in f:
    count += len(line.split())
    
print("The file has", count, "words.")   