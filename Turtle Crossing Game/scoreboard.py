from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(-280, 250)
        self.scoreboard.write(arg=f"Level: {self.level}", font=FONT)

    def update_level_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(arg=f"Level: {self.level}", font=FONT)

    def increment_level(self):
        self.level += 1