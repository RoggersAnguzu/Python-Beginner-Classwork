# -*- coding: utf-8 -*-
from random import randint
secret = randint(1, 10)

for i in range(5):
    guess = int(input("Guess a number between 1 and 10: "))
    if not guess == secret:
        print("Try agian!")
    else:
        print("You win!")
        
print("The answer is", secret)