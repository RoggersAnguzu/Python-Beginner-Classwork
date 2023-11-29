# Question 2.1

temp = float(input('Enter a temperature in Celsius: '))
ftemp = 9/5 * temp + 32
print('Celsius:', temp)
print('Fahrenheit:', ftemp)

# Question 2.2

temp = float(input('Enter a temperature in Celsius: '))
ftemp = 9/5 * temp + 32
print('Celsius:', temp)
print('Fahrenheit:', ftemp)
#if ftemp < 97 or ftemp > 99: print('Abnormal')
if ftemp >= 97 and ftemp <= 99: # 97<=ftemp<=99 
    print("Normal")
else:
    print("Abnormal")

# Question 2.3
temp = float(input('Enter a temperature in Celsius: '))
if temp < 0:
    print("Invalid input")
else:
    ftemp = 9/5 * temp + 32
    print('Celsius:', temp)
    print('Fahrenheit:', ftemp)

    
