
from turtle import Turtle
ALIGN="center"
FONT =("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score,align=ALIGN, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score,align=ALIGN, font=FONT)