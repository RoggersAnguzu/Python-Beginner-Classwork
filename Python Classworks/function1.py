from math import sqrt

# Function definition
def sqr(n):
    return n * n

# Calling or invoking the function
x = 3
y = 4

xsqrd = sqr(x)
ysqrd = sqr(y)

print("The lenght of the hypotenuse is", \
      sqrt(xsqrd + ysqrd) )
# You can put a function call anywhere
# a number is expected, as long as
# that function returns a number   
print("The length of the hyp is:", sqrt(sqr(x) + sqr(y)))