import turtle

def drawSquare(t, sz, border_color, fill_color, x, y):
    """Make turtle t draw a square of with side sz."""

    t.begin_fill()

    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.color(border_color)
    
    for i in range(4):
        t.forward(sz)
        t.left(90)

    t.color(fill_color)
    t.end_fill()

    t.penup()
    t.home()


        
    

wn = turtle.Screen()
wn.bgcolor("blue")

t = turtle.Turtle()
sz = 50
border_color = "yellow"
fill_color = "grey"
x = 100
y = 100

drawSquare(t, sz, border_color, fill_color, x, y)

wn.exitonclick()


