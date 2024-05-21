import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_obj = Player()
scoreboard_obj = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=turtle_obj.move_forward)

car_managerObj = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_managerObj.create_cars()
    car_managerObj.move_cars()
    if turtle_obj.timmy.ycor() >= FINISH_LINE_Y:
        turtle_obj.timmy.setposition(STARTING_POSITION)
        scoreboard_obj.increment_level()
        scoreboard_obj.update_level_scoreboard()
    for car in car_managerObj.all_cars:
        if car.distance(turtle_obj.timmy) < 20:
            game_over = Turtle()
            game_over.hideturtle()
            game_over.write(arg="GAME OVER", font=("Courier", 48, "normal"), align="center")
            game_is_on = False

screen.exitonclick()