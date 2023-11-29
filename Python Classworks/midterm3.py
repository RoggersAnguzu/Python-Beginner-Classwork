# Question 3.1
sentence = input("Enter a sentence: ")
if len(sentence) < 5:
    print("Too short")
else:
    print(sentence[-5:])
    
# Question 3.2
choice = input("What would you like: tea, coffee, water? ")
print("Here is you", choice)