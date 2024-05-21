import random
import time
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(250, random.randint(-200, 200))
            car.setheading(0)
            car.shapesize(1, 2)
            self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)