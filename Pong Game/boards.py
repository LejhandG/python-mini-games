from turtle import Turtle, Screen

class Boards:
    def __init__(self, setx, sety, keybind1, keybind2):
        self.board = Turtle("square")
        self.board.penup()
        self.board.setpos(x=setx, y=sety)
        self.board.shapesize(10, 1)
        self.board.color("white")

    def front(self):
        if self.board.ycor() != 200:
            self.board.goto(x=self.board.xcor(), y=self.board.ycor() + 10)

    def back(self):
        if self.board.ycor() != -190:
            self.board.goto(x=self.board.xcor(), y=self.board.ycor() - 10)