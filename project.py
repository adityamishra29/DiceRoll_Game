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
    
    
    
