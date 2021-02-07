from turtle import Turtle
from food import Food

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.colision = False
        super().__init__()
        self.get_score(self.score)
        
    
       
    def get_score(self, score):
        self.hideturtle()
        self.penup()
        self.goto(0 , 285)
        self.color("white")
        self.write(f"Score: {score}" , move=True, font=('monaco', 10 , 'bold'), align='center')
        
    def update_score(self):
        self.score += 1
        self.reset()
        self.get_score(self.score)
        
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0 , 0)
        self.color("white")
        self.write("GAME OVER" , move=True, font=('monaco', 30 , 'bold'), align='center')   
        