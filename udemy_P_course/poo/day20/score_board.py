from turtle import Turtle
PATH = "C:/Users/megaw/Desktop/Dev/Python/udemy_P_course/poo/day20/data.txt"
class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open(PATH, "r+") as self.file:
            self.content = self.file.read()
        
        
        self.high_score = int(self.content)
        self.colision = False
        super().__init__()
        self.get_score(self.score)
        
    
       
    def get_score(self, score):
        self.hideturtle()
        self.penup()
        self.goto(0 , 285)
        self.color("white")
        self.write(f"Score: {score}  High Score: {self.high_score}" , move=True, font=('monaco', 10 , 'bold'), align='center')
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.get_score(self.score)
        
        
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score )
            with open(PATH, "r+") as text:
                text.write(self.high_score)
        self.score = 0   
        self.update_score()
            
    # def game_over(self):
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0 , 0)
    #     self.color("white")
    #     self.write("GAME OVER" , move=True, font=('monaco', 30 , 'bold'), align='center')   
        