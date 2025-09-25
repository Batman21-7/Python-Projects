from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed(10)


def forward():
    tim.forward(10)


def back():
    tim.back(10)


def right():
    tim.rt(10)


def left():
    tim.lt(10)


def clear():
    tim.reset()


screen.listen()

screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=back)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
