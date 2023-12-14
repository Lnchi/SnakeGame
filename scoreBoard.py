from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=300)
        self.update()
    def update(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
    def increase(self):
        self.score += 1
        self.clear()
        self.update()
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGN, font=FONT)




