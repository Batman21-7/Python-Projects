from turtle import Screen
from player import Player
from car import Car
from scoreboard import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

game_is_on = True

player = Player()
car = Car()
level = Level()

screen.listen()
screen.onkey(fun=player.move, key='Up')
screen.onkey(fun=player.down, key='Down')

while game_is_on:
    car.move()

    if player.ycor() > 260:
        level.update_level()
        player.restart()
        car.move_speed += 5

    for i in car.cars:
        if abs(player.xcor()-i.xcor()) < 29 and abs(player.ycor()-i.ycor()) < 19:
            level.game_over()
            game_is_on = False
            break

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
