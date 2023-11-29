# -*- coding: utf-8 -*-
from random import randint
secret = randint(1, 5)

for i in range(5):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != secret:
        print("Try agian!")
    else:
        print("You win!")
        break
        
print("The answer is", secret)