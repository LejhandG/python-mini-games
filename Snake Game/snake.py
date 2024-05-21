import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

food = Turtle("circle")
food.penup()
food.color("Red")
food.setpos(random.randint(-200, 200), random.randint(-200, 200))

title = Turtle()
title.penup()
title.hideturtle()
title.color("White")
title.goto(0, 250)

game_over = Turtle()
game_over.penup()
game_over.hideturtle()
game_over.color("White")
game_over.goto(0, 0)


def move_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)


def move_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)
    
def move_up():
    if segments[0].heading() != 270:
        segments[0].setheading(90)

def move_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

score = 0
title.write(f"Score: {score}", align="center", font=("candara", 24, "bold"))

screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)

game_is_on = True
while game_is_on:
    if segments[0].distance(food.pos()) <= 15:
        food.setpos(random.randint(-200, 200), random.randint(-200, 200))
        score += 1
        title.clear()
        title.write(f"Score: {score}", align="center", font=("candara", 24, "bold"))

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segments[-1].position())
        segments.append(new_segment)

    if abs(segments[0].xcor()) >= 300 or abs(segments[0].ycor()) >= 300:
        game_is_on = False
        game_over.write(f"Game Over", align="center", font=("candara", 48, "bold"))


    for seg_num in range(1, len(segments)):
        if segments[0].distance(segments[seg_num].pos()) < 10:
            game_is_on = False
            game_over.write(f"Game Over", align="center", font=("candara", 48, "bold"))
            break

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

    screen.update()

screen.exitonclick()