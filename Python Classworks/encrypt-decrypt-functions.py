# Encrypt function
def encrypt(message):
    code = ''
    for c in message:
        code = code + " " + str(ord(c))
    return code


# Decrypt function
def decrypt(code):
    original = ''
    code = code.split()
    for ascii in code:
        original = original + chr(int(ascii))
    return original

def main():
    message = input("Enter your message: ")
    secret = encrypt(message)
    print(secret)
    print(decrypt(secret))
    
main()