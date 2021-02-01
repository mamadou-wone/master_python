# import turtle
# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# # timmy.forward(100)
# timmy.color("green")
# timmy.speed("normal")
# while  True:
#     timmy.circle(100)
# my_screen = Screen()


# my_screen.exitonclick()

# print(my_screen.canvheight)
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachou", "Squirtle" , "Charmander"])
table.add_column("Type", ["Electric", "Water" , "Fire"])
table.align = "l"



print(table)