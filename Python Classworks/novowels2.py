vowels = 'aeiou'
message = "This is top secret."
secret = ''
for c in message:
    if c not in vowels:
        secret = secret + c
print(secret)