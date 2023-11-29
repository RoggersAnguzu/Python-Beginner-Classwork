score = float(input("Enter the numeric score: "))

while score < 0 or score > 100:
    print("The score must be in the range [0-100]")
    score = float(input("Enter the numeric score: "))

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