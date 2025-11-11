from turtle import Turtle, Screen,colormode
import random

tinny_the_turtle = Turtle()
tinny_the_turtle.shape("arrow")
tinny_the_turtle.color("black")
tinny_the_turtle.speed(20)
tinny_the_turtle.pensize(4) 
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colors = (r, g, b)
    return random_colors

def spirograph():
    for i in range(40):
        tinny_the_turtle.color(random_color())
        tinny_the_turtle.circle(100)
        tinny_the_turtle.setheading(tinny_the_turtle.heading() + 10)


spirograph()


screen = Screen()
screen.exitonclick()