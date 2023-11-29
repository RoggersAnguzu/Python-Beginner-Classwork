vowels = 'aeiou'
message = input("Enter your message: ")
sms =''
for letter in message:
    if letter not in vowels:
        sms = sms + letter
   
print(sms)
