FONT = ("Courier", 18, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_score()

    def get_score(self):
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.write(f"Level: {self.score}" , font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.reset()
        self.get_score()
        
        
    def game_over(self):
        self.penup()
        self.goto(0 , 0)
        self.hideturtle()
        self.write("GAME OVER", font=FONT)