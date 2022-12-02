#Design a project where as an input student will give a static number (between 1 to 6) and then
#roll the dice which randomly generate some value between 1 to 6. The winning situation arrives
#when the given static/fixed number exactly same to the number came after rolling the dice.
#User can play the game as many numbers of times he wants until user wants to exit, and
#whenever winning situation occur some scores must be given to the user, and these scores goes
#on adding if user play this game multiple number of times.
#Note: Dice contains face value’s (1 to 6)
#Hint: Make use of random.randint() function
import random

print("Welcome to DICE NUMBER PREDICTION GAME!")

i = ""
scr = 0

while i!="n":
    x = int(input("Enter a Number from 1 to 6 : "))
    y = random.randint(1, 6)
    if 1<=x<=6:
        print(x,y)
        if x==y:
            scr+= 10
    else:
        print("Enter a number between 1 to 6")
    i = str(input("Do you want to continue the game? \nEnter n if you do not want to continue the game: \nEnter y if you want to continue the game: "))

print("Game Exited!")
print("Score:", scr)             
    
    
    
