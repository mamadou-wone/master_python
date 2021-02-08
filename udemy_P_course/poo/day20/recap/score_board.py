from turtle import Turtle
FONT=("Arial", 12, "bold")
class ScorBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.colision = False
        super().__init__()
        self.get_score()
        
    def get_score(self):
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"Score: {self.score}" ,True, font=FONT, align="center")
        
    def update_score(self):
        self.colision = True
        if self.colision:
            self.score += 1
            self.reset()
            self.get_score()
            
    def game_over(self):
        self.goto(0 , 0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER :(" ,True, font=FONT, align="center")