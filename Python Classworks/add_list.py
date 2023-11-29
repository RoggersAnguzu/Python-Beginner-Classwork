lst = [1, 2, 3, 2, 6, 7, 9, 1]

# Method 1
total = 0
for i in range(len(lst)):
    total = total + lst[i]
    
print(total)

# Method 2
total = 0
for item in lst:
    total = total + item

print(total)

# Method 3
print(sum(lst))