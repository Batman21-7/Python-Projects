from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")

screen.tracer(0)

game_is_on = True

p1_paddle = Paddle((-350,0))
p2_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=p1_paddle.Up, key='w')
screen.onkeypress(fun=p1_paddle.Down, key='s')
screen.onkey(fun=p2_paddle.Up, key='Up')
screen.onkey(fun=p2_paddle.Down, key='Down')

while game_is_on:

    # Ball bounce of top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Ball bounce off paddle
    if ball.distance(p2_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
    elif ball.distance(p1_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Check if ball hit right or left wall and reset
    if ball.xcor() > 380:   # right
        ball.restart()
        scoreboard.l_score += 1
        scoreboard.update()
    elif ball.xcor() < -380:  # left
        ball.restart()
        scoreboard.r_score += 1
        scoreboard.update()

    ball.move()
    
    time.sleep(ball.move_speed)
    screen.update()

screen.exitonclick()
