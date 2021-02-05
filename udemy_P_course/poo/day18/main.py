from turtle import Turtle,Screen
import random
# from turtle import *


# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# colors  = ["red","green","blue","orange","purple","pink","yellow"]
# screen = Screen()
# screen.colormode(255)
"""
Sqare drawing
"""
# for _ in range(4):
#     timmy.forward(180)
#     timmy.left(90)

# timmy.goto(0, 70)
# for _ in range(15):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()


# number = 3




# def draw_figure(number, colors = []):
#     angle = 360 / number
#     color =random.choice(colors)
#     for _ in range(number):
#         timmy.forward(100)
#         timmy.left(angle)
#         timmy.color(color)
    
# for i in range(3, 11):
#     draw_figure(i, colors)
    

"""WONE"""
# timmy.goto(-35 , 90)
# timmy.home()
# timmy.goto(10, 25)
# timmy.goto(20 , 0)
# timmy.goto(40, 90)
# timmy.up()
# timmy.goto(80 , 0)
# timmy.down()
# timmy.circle(30)
# timmy.up()
# timmy.goto(130, 0)
# timmy.down()
# timmy.goto(130, 90)
# timmy.goto(160, 0)
# timmy.goto(160,90)
# timmy.goto(160 ,0)
# timmy.up()
# timmy.goto(200,0)
# timmy.down()
# timmy.goto(200 , 90)
# timmy.goto(250, 90)
# timmy.goto(200 , 90)
# timmy.goto(200 , 50)
# timmy.goto(250, 50)
# timmy.goto(200 , 50)
# timmy.goto(200 , 0)
# timmy.goto(250, 0)


"""Random WALK"""
# for _ in range(100):
#     color = random.choice(colors)
#     number = random.randint(0, 1)
#     if number == 0:
#             timmy.left(90)
#     else:
#         timmy.right(45)
#     timmy.pensize(5) 
#     timmy.color(color)       
#     timmy.forward(15)        

# timmy.pensize(5)

# def gen_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r , g , b)
    
    
    
# for i in range(100):
#     timmy.speed("fastest")
#     timmy.color(gen_color())
#     timmy.circle(60)
#     timmy.left(i)
    # timmy.circle(60)
# timmy.right(180)
# timmy.left(10)

# def draw_sparographe(size):
#     for _ in range(int(360 / size)):
#         timmy.speed("fastest")
#         timmy.color(gen_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size)

# draw_sparographe(5)        
# colors = colorgram.extract("./udemy_P_course/poo/turtle/color.jpg", 6)
# option = []

# for i in range(len(colors)):
#     option.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
    
import colorgram
colors = [(204, 116, 163), (152, 154, 201), (204, 0, 4), (171, 176, 4), (89, 68, 4), (171, 95, 188)] 

boss = Turtle()
boss.speed('fastest')
boss.hideturtle()
screen = Screen()    
screen.colormode(255)

def gen_color(colors = []):
    return random.choice(colors)


def test():
    x = 30
    while x <= 300:
        for _ in range(10):
            boss.up()
            boss.dot(20 , gen_color(colors))
            boss.forward(50)
        
        boss.goto(0, x)
        x += 30   
test()   
# answer = input(" Response ? ")

# if answer == "A":
#     test()
# else:
#     print("NOOOOOOOOOOOOOOO")        
    
    
    
    
    
    
    
    
    
    
    
    


















screen.exitonclick()