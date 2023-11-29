score = float(input("Enter the numeric score: "))

while True:
    if score < 0:
        print("The score must be 0 or greater.")
        score = float(input("Enter the numeric score: "))
    elif score > 100:
        print("The score must be 100 or less.")
        score = float(input("Enter the numeric score: "))
    else:
        break

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')