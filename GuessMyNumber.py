#Automate the Boring Stuff
#Programming practice
#Regina Gates, July 17, 2017
#Unless marked with -AS, the comments are my own notes from or about the material.

#This is a guess the number game. -AS
# We need to randomize the select number, so import the random module.
import random

print("Hello! What is your name?")
name = input()
secretNumber = random.randint(1, 20) # 1 and 20 are included
print("Well, " + name + ", I am thinking of a number between 1 and 20. Can you guess it?")

for guessesTaken in range(1, 7):
#This For loop is used because want a certain number of iterations. We could
# specify range(6), but the from--to range is useful, as well. 7 is not included.
# The for loop will track the value of guessesTaken.

    print('Take a guess.')
    guess = int(input()) #this value is a string, so we need to convert to int.

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This condition is for the correct guess! -AS
    #The else statement is unnecessary when the range is reached, because the loop
    #will naturally terminate.

if guess == secretNumber:
    print('Good job, '+ name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
    #guessesTaken is an int value and must be converted to a string for concatenation.

else:
    print('Nope! The number I was thinking of was ' + str(secretNumber) + '!')
    
