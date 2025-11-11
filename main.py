from turtle import Turtle, Screen
from Paddle import paddle
from Ball import ball
from Score import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600 )
screen.bgcolor("black")
screen.title("Pong")
tim = Turtle()
screen.tracer(0)
r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))
ball = ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() >  340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if  ball.xcor() > 375:
        ball.reset_ball()
        score.score_l()


    if ball.xcor() < -375:
        ball.reset_ball()
        score.score_r()


    #if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #   game_on = False
    #   scoreboard.game_over()
screen.exitonclick()









