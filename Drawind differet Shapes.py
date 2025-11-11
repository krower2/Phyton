from turtle import Turtle, Screen
import random
tinny_the_turtle = Turtle()
tinny_the_turtle.shape("arrow")
tinny_the_turtle.color("black")

colours = ["red", "blue", "green", "yellow", "cyan", "purple"]



def drawing_all():
    form_shape = 3
    turtle_game = True
    while turtle_game:
        tinny_the_turtle.color(random.choice(colours))
        for i in range(form_shape):
            tinny_the_turtle.forward(50)
            tinny_the_turtle.right(360 / form_shape)

        form_shape += 1
        if form_shape == 10:
            turtle_game = False




drawing_all()
screen = Screen()
screen.exitonclick()