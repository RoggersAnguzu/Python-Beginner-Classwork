message = "The money is under the pillow."

# Encrypt
code = ''
for c in message:
    code = code + " " + str(ord(c))
    
print(code)

# Decrypt
original = ''
code = code.split()
for ascii in code:
    original = original + chr(int(ascii))

print(original)