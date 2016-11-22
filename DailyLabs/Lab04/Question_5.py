import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()

length = 150 * .381

alex.penup()
alex.left(90)
alex.forward(71.329)
alex.right(90)

alex.pendown()
alex.right(72)
alex.forward(length)
alex.left(72)
alex.forward(length)
alex.right(144)
alex.forward(length)
alex.left(72)
alex.forward(length)
alex.right(144)
alex.forward(length)
alex.left(72)
alex.forward(length)
alex.right(144)
alex.forward(length)
alex.left(72)
alex.forward(length)
alex.right(144)
alex.forward(length)
alex.left(72)
alex.forward(length)
alex.penup()

alex.home()

wn.exitonclick()
