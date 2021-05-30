#  The Perfect Guess
# we are going to write a program that generates a random number and asks the user to guess it.
# If the player guess is higher than the actual number, the program displays "Lower number please
# similary if the user guess is too low the peogram printe "highre number please"
# when the user guess the correct number , the program display the number of guess the player used to arive at the number.

import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if (userGuess == randNumber):
       print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")


print(f"You guessed the number in {guesses} guesses")
    
