from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)
screen.listen()

score = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
playing = True
while playing:
    screen.update()
    ball.move()
    time.sleep(ball.pace)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.I_l_score()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.I_r_score()


screen.exitonclick()
