from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width =500, height = 400)

colors = ["red" , "orange", "yellow" , "green" , "blue", "purple"]

user_bet = screen.textinput("Winner", "Which turtle will win ? Enter the color: ")
all_turtle = []
is_on = False


def random_position():
    return random.randint(0 , 10)


y = 150    
for t_color in colors:
    boss = Turtle("turtle")
    boss.color(t_color)
    boss.penup()
    boss.goto(-230 , y)
    y -= 50
    all_turtle.append(boss)


 
if user_bet:
    is_on = True
  
 
while is_on:
    
    for item in all_turtle:
        if item.xcor() > 230:
           is_on = False
           winning_color = item.pencolor()
           if winning_color == user_bet:
               print("You win")
           else:
            print(f"You loose and the winner color is {winning_color}")   
           
           
        position = random_position()
        item.forward(position)
                




screen.exitonclick()