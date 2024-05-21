from turtle import Turtle
class CenterLine:
    def __init__(self):
        self.center_line = Turtle()
        self.center_line.hideturtle()
        self.center_line.penup()
        self.center_line.setpos(0, -300)
        self.center_line.pensize(20)
        self.center_line.pencolor("white")
        self.center_line.left(90)
        for i in range(1, 12):
            self.center_line.pendown()
            self.center_line.forward(20)
            self.center_line.penup()
            self.center_line.forward(40)