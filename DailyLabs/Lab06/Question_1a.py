import turtle

def drawSquare():
    """Make turtle t draw a square of with side sz."""

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    alex = turtle.Turtle()
    sz = 50
    
    for i in range(4):
        alex.forward(sz)
        alex.left(90)

    wn.exitonclick()

drawSquare()
