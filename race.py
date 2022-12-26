from time import sleep
import turtle
import random

player1=turtle.Turtle()
player1.color('Orange')
player1.shape('turtle')
player1.penup()
player1.goto(-200,100)
player2=player1.clone()
player2.color('Green')
# player2.penup()
player2.goto(-200,-100)
player1.goto(300,60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200,100)
player2.goto(300,-120)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200,-100)
player2.pendown()
player1.pendown()
die=[1,2,3,4,5,6]
players_name=[]
for i in range(1,3):
    name=turtle.textinput("Player name",f"{i} player name")
    players_name.append(name)
for i in range(20):
    if player1.pos()>=(300,60):
        turtle.hideturtle()
        turtle.write(f"{players_name[0]} Wins", align="center", font=("Cooper Black", 25, "italic"))

    elif player2.pos()>=(300,-120):
        turtle.hideturtle()
        turtle.write(f"{players_name[1]} Wins", align="center", font=("Cooper Black", 25, "italic"))
    else:
        player1_turn=input("Press enter to roll the dice ")
        die_outcome=random.choice(die)
        print(f"The result of the die roll is:{die_outcome}")
        print("The number of steps will be:")
        print(20*die_outcome)
        player1.forward(20*die_outcome)
        player2_turn=input("Press enter to roll the dice ")
        die_outcome=random.choice(die)
        print(f"The result of the die roll is:{die_outcome}")
        print("The number of steps will be:")
        print(20*die_outcome)
        player2.forward(20*die_outcome)         

sleep(5)

