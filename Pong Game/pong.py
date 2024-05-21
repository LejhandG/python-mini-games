from turtle import Turtle, Screen
from center_line import CenterLine
from boards import Boards
from ball import Ball

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

center_line = CenterLine()

board1 = Boards(-350, 0, "w",  "s")
board2 = Boards(350, 0, "Up", "Down")

ball = Ball()
score1 = 0
score2 = 0
title = Turtle()
title.penup()
title.hideturtle()
title.color("White")
title.goto(0, 250)
title.write(f"{score1}            {score2}", align="center", font=("candara", 24, "bold"))

screen.listen()
screen.onkeypress(key="w", fun=board1.front)
screen.onkeypress(key="s", fun=board1.back)
screen.onkeypress(key="Up", fun=board2.front)
screen.onkeypress(key="Down", fun=board2.back)

game_is_on = True
while game_is_on:
    ball_obj = ball.ball
    ball.move()
    if ball_obj.ycor() > 290 or ball_obj.ycor() < -290:
        ball.bounce_y()
    if ball_obj.distance(board2.board) < 50 and ball_obj.xcor() > 340:
        ball.bounce_x()
    if ball_obj.distance(board1.board) < 50 and ball_obj.xcor() < -340:
        ball.bounce_x()
    if ball_obj.xcor() > 390:
        title.clear()
        score1 += 1
        title.write(f"{score1}            {score2}", align="center", font=("candara", 24, "bold"))
        ball.reset()
    if ball_obj.xcor() < -390:
        title.clear()
        score2 += 1
        title.write(f"{score1}            {score2}", align="center", font=("candara", 24, "bold"))
        ball.reset()

screen.exitonclick()