from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.timmy = Turtle(shape="turtle")
        self.timmy.penup()
        self.timmy.goto(STARTING_POSITION)
        self.timmy.setheading(90)

    def move_forward(self):
        self.timmy.forward(MOVE_DISTANCE)