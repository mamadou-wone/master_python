from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.show_score()
    
                
    def show_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100 , 200)
        self.write(self.l_score , move=True, font=('monaco', 70 , 'bold'), align='center')
        self.goto(100 , 200)
        self.write(self.r_score , move=True, font=('monaco', 70 , 'bold'), align='center')  
     
    # def l_score_increase(self):
    #     self.reset()
    #     self.l_score += 1        
    #     self.show_score()