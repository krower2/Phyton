from turtle import Turtle, Screen,colormode
import random
tinny_the_turtle = Turtle()
tinny_the_turtle.shape("arrow")
tinny_the_turtle.color("black")
tinny_the_turtle.pensize(4)
tinny_the_turtle.speed(10)
directions = [0, 90 , 180 , 270]
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colors = (r, g, b)
    return random_colors


def random_walk():
    walk_time = 50
    for i in range(walk_time):
        tinny_the_turtle.color(random_color())
        tinny_the_turtle.forward(30)
        tinny_the_turtle.setheading(random.choice(directions))

random_walk()

screen = Screen()
screen.exitonclick()