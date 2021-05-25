# creating a game  Rock , Paper , scissors
import random

def gameWin(computer , you):
    if computer == you:  #if two values are equal , declare a tie
        return None

    # check for all possiblities when computer chose r = Rock
    elif computer == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    # check for all possiblities when computer chose s = scissors
    elif computer == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

    # check for all possiblities when computer chose p = paper
    elif computer == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

print("Computer Turn: Rock(r) Paper(p) Scissors(s)? ")
randNO = random.randint(1,3)
if randNO == 1:
    computer = 'r'
elif randNO == 2:
    computer = 'p'
elif randNO == 3:
    computer = 's'


you = input("Your Trun: Rock(r) Paper(p) Scissors(s)? ")
a = gameWin(computer , you)

print(f"Computer Chose {computer}")
print(f"You Chose {you}")

if a == None:
    print("The Game is Tie!")
elif a:
    print("You Win ")
else:
    print("You Lose ")