n = int(input("What is end point? "))
total = 0

print("Using the for loop")
for i in range(1, n+1):
    total = total + i

   
print("The sum from 1 to", n, "is", total)

print("Now using the while loop")
i = 1
total = 0
while i <= n:
    total = total + i
    i = i + 1
print("The sum from 1 to", n, "is", total)