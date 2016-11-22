import turtle

def drawSquare(t, sz, bordercolor):
    """Make turtle t draw a square of with side sz."""

    t.color(bordercolor)
    
    for i in range(4):
        t.forward(sz)
        t.left(90)


        
    

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
sz = 50
bordercolor = "yellow"

drawSquare(t, sz, bordercolor)

wn.exitonclick()


