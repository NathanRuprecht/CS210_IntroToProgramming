import turtle

def drawSquare(t, sz, border_color, fill_color):
    """Make turtle t draw a square of with side sz."""

    for i in range(36):
        t.begin_fill()
        t.color(border_color)


        for i in range(4):
            t.forward(sz)
            t.left(90)   

        t.color(fill_color)
        t.end_fill()
        
        t.right(10)    


        
    

wn = turtle.Screen()
wn.bgcolor("blue")

t = turtle.Turtle()
sz = 50
border_color = "yellow"
fill_color = "grey"

drawSquare(t, sz, border_color, fill_color)

wn.exitonclick()


