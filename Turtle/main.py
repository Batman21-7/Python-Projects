import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')

"""shapes 3 sided to 1100000"""
# print(turtle.colormode())
# timmy.speed(10)
# for i in range(3, 1100000):
#     timmy.pencolor((random.random(), random.random(), random.random()))
#     for j in range(i):
#         timmy.fd(10)
#         timmy.rt(360/i)

"""Random walk"""
# timmy.pensize(10)
# timmy.speed(10)
# while True:
#     timmy.pencolor((random.random(), random.random(), random.random()))
#     timmy.setheading(random.choice([0, 90, 180, 270]))
#     timmy.fd(50)

"""spirograph"""
# timmy.speed(0)
# for i in range(100):
#     timmy.pencolor((random.random(), random.random(), random.random()))
#     timmy.circle(100)
#     timmy.rt(3.6)

screen = Screen()
screen.exitonclick()