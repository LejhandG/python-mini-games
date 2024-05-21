from turtle import Turtle

class Score:
    score1 = 0
    score2 = 0
    def __init__(self):
        self.title = Turtle()
        self.title.penup()
        self.title.hideturtle()
        self.title.color("White")
        self.title.goto(0, 250)
        self.title.write(f"{self.score1}            {self.score2}", align="center", font=("candara", 24, "bold"))

    def inc_p1(self):
        self.score1 += 1
        self.title.clear()
        self.title.write(f"{self.score1}            {self.score2}", align="center", font=("candara", 24, "bold"))

    def inc_p2(self):
        self.score2 += 1
        self.title.clear()
        self.title.write(f"{self.score1}            {self.score2}", align="center", font=("candara", 24, "bold"))