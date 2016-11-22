import turtle

def drawSquare(sz):
    """Make turtle t draw a square of with side sz."""

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    t = turtle.Turtle()

    for i in range(4):
        t.forward(sz)
        t.left(90)

    wn.exitonclick()
        
    


sz = 50

drawSquare(sz)


