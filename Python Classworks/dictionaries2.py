numbers = {'one': 1, 'two': 2,
           'three': 3, 'four': 4}
lst1 = ['five', 'six', 'seven', 'eight']
lst2 = [5, 6, 7, 8]

for i in range(len(lst1)):
    numbers[lst1[i]] = lst2[i]
    
print(numbers)

print(numbers['four'])