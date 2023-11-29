f = open('numbers2.txt', 'w')
for i in range(1, 11):
    f.write(str(i) + "\n")
f.close()