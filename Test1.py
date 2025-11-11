from turtle import Turtle, Screen
import prettytable

# timmy = Turtle()
# # print(timmy)
# timmy.shape("turtle")
# timmy.color('blue')
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


table = prettytable.PrettyTable()
table.field_names = ["Pokemon Table", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squiertle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)





