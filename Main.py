from turtle import Turtle, Screen
import heroes


tinny_the_turtle = Turtle()
tinny_the_turtle.shape("arrow")
tinny_the_turtle.color("red")
def triangle ():
    tinny_the_turtle.forward(100)
    tinny_the_turtle.left(120)
    tinny_the_turtle.forward(100)
    tinny_the_turtle.left(120)
    tinny_the_turtle.forward(100)

def square():
    for i in range(4):
        tinny_the_turtle.forward(100)
        tinny_the_turtle.left(90)

def dashed_line():
    for i in range(7):
        tinny_the_turtle.forward(10)
        tinny_the_turtle.penup()
        tinny_the_turtle.forward(10)
        tinny_the_turtle.pendown()

triangle()
square()

screen = Screen()
screen.exitonclick()

