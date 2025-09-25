# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# RGBcolors = []
# for i in colors:
#     temp = i.rgb
#     RGBcolors.append((temp.r, temp.g, temp.b))

import turtle
from turtle import Turtle
from random import choice

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
              (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
              (0, 63, 145), (173, 135, 162), (7, 172, 216),(158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
              (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

turtle.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.speed(0)
timmy.hideturtle()

timmy.goto(-300, -300)
y = -300

for _ in range(10):
    timmy.goto(-300, y)
    for _ in range(10):
        timmy.dot(20, choice(color_list))
        timmy.fd(50)
    y += 50

turtle.mainloop()