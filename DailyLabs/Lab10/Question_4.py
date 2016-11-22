import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound-50 or turtleX < leftBound+50:
        stillIn = False
    if turtleY > topBound-50 or turtleY < bottomBound+50:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(1, 3, 1)
    if coin == 0:
        t.left(4)
    elif coin == 1:
        t.right(8)
    else:
        t.right(0)

    t.forward(2)

wn.exitonclick()
