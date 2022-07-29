# A guessing game implemented by importing the random function

import random

def guess(x) :
    random_number = random.randint(1,x)
    pick = 0     #initialize guess variable
    while pick != random_number :
        pick = int(input(f'Guess a number between 1 and {x}: '))
        if pick < random_number :
            print('Sorry, guess again. Too low')
        elif pick > random_number :
            print('Sorry, guess again. Too high ')
    
    print(f'Hurray, congrats. You guessed the number {random_number} correctly')

guess(15)