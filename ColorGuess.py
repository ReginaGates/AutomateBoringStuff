#Guess my color, inspired by
#Automate the Boring Stuff with Python -Al Sweigert
#and
#The Self-Taught Programmer by Cory Althoff

import random

print('What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of one of the rainbow colors. Can you guess it in 3 guesses?')

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
colorIndex = random.randint(1, 6)
secretColor = rainbow[colorIndex]

#print('DEBUG: The color is ' + secretColor + '.')

for colorGuess in range(1,4):
    print('Take a guess.')
    guess = input()

    if guess != secretColor:
        i = 3 - colorGuess
        if i==0:
            break
        print('Nope! Try again! You have ' + str(3 - colorGuess) + ' guesses left.')
    else:
        break
    
if guess == secretColor:
    print('Wow! Congratulations, ' + name + '! You guessed my color in ' + str(colorGuess) + ' guesses!')

else:
    print('No, sorry! The correct answer is ' + secretColor + '.')

    
   
