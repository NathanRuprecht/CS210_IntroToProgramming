import turtle

def drawSquare(t):
    """Make turtle t draw a square of with side sz."""

    sz = 50
    
    for i in range(4):
        t.forward(sz)
        t.left(90)





wn = turtle.Screen()
wn.bgcolor("lightgreen")
    
alex = turtle.Turtle()

drawSquare(alex)

wn.exitonclick()
