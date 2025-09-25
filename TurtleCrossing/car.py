from turtle import Turtle
from random import random, randint


class Car():
    def __init__(self):
        self.move_speed = 10
        self.cars = []
        for _ in range(15):
            self.add_car(randint(-300, 200))

    def add_car(self, x):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random(), random(), random())
        new_car.goto(x, randint(-200, 200))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):
        i = 0
        while i < len(self.cars):
            if self.cars[i].xcor() < -330:
                self.cars.remove(self.cars[i])
                self.add_car(250)
            else:
                self.cars[i].forward(self.move_speed)
            i += 1
