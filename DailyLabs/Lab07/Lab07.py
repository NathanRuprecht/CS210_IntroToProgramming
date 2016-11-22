#Go to 'Main' on line 195 to test questions 2, 3, or 5




#
#Question 1:
#   Returns:
#       -turtle.stamp() returns a stamp id so in the future we can
#       reference/delete
#       -turtle.speed() returns the current speed if none is specified
#       -turtle.pos() returns the x and y coordinates of the turtle's
#       current position
#   Does not return:
#       -turtle.forward() doesn't need to return because it's a one time
#       event
#       -turtle.back() also doesn't need to return because it's a one
#       time event
#       -turtle.right() doesn't need to return because it's a one time
#       event
#

import math
import turtle




#Question 2 to be called in Main
def Question_2():
    """Implement a function called circleArea that calculates the area
of a circle given the circle’s radius. Have the function print the value
of the area and return nothing to the calling program. Verify that the
function is working correctly by calling the function several times with
different radius values. """

    #define constants
    RADIUS = 10


    #call function circlearea
    CircleArea(RADIUS)

def CircleArea(r):
    area = (math.pi) * (r ** 2)
    print(area)






#Question 3 to be called in Main
def Question_3():
    """Make a copy of your python program for exercise 2 and change the
function so that it prints nothing and returns the area value it
calculated. Verify that the function is working correctly by calling the
function several times with different radius values. Note that you will
have to make the calling program print out the value."""       

    #define constants
    RADIUS = 10


    #call function circlearea to print area
    CircleArea2(RADIUS)
    
    result = CircleArea2(RADIUS)
    print(result)

def CircleArea2(r):
    area = (math.pi) * (r **2)
    return area




#Question 5i to be called in Main
def Question_5i():
    """Fairly simple math will calculate the sides and angles of the
inside square. If we assume that the distance “a” is some fraction of
the size of the blue square the calculations are:
    a = fraction * size
    b = size – a
    size’ = sqrt(a2 + b2)
    α = tan-1(a/b) (in python, atan2(a,b))
Implement a function that will draw the red square. The 
function should have 3 input parameters: a turtle, the size of the blue square, and the 
fraction used to calculate “a”."""

    #define constants and make graphics window
    wn = turtle.Screen()
    wn.bgcolor("white")
    t = turtle.Turtle()
    
    FRACTION = (1/5)
    SIZE = 60


    #math needed to draw squares
    a = FRACTION * SIZE
    b = SIZE - a
    SIZE2 = math.sqrt( a**2 + b**2)
    alpha = math.degrees(math.atan2(a,b))


    #draw the blue, then red squares
    drawSquares(t, SIZE, SIZE2, b, alpha)
    wn.exitonclick()


def drawSquares(t, SIZE, SIZE2, b, alpha):

    #draw blue square
    t.color("blue")
    for i in range(4):
        t.forward(SIZE)
        t.left(90)

    #draw red square
    t.color("red")
    TURN = 90 - alpha
    t.penup()
    t.forward(b)
    t.pendown()
    t.left(180)
    t.right(alpha)
    for i in range(4):
        t.forward(SIZE2)
        t.right(90)





#Question 5ii to be called in Main
def Question_5ii():
    """Now let’s use the previous function to draw multiple inside squares
Create a new function that draws multiple squares inside a square. This
function should also have three parameters: a turtle, the size of the
outside square, and the number of inside squares to draw. This function
should call the function you have already created to draw an inside square
You should now be able to draw shapes that look like the figures to the
right. The shapes have 2, 4, and 9 inside squares."""

    #define constants and make graphics window
    wn = turtle.Screen()
    wn.bgcolor("white")
    t = turtle.Turtle()
    
    FRACTION = (1/5)
    SIZE = 60


    #math needed to draw squares
    a = FRACTION * SIZE
    b = SIZE - a
    SIZE2 = math.sqrt( a**2 + b**2)
    alpha = math.degrees(math.atan2(a,b))


    #draw the blue squares
    drawSquares(t, SIZE, SIZE2, b, alpha)
    wn.exitonclick()


def drawSquares(t, SIZE, SIZE2, b, alpha):

    #draw main square
    t.color("blue")
    for i in range(4):
        t.forward(SIZE)
        t.left(90)

    #draw other squares





#Main
#Question_2()
#Question_3()
#Question_5i()
#Question_5ii()




#
#Question 4:
#   i: Yes on exercise 2. No on exercise 3 because you haven't printed the
#       returned value.
#   ii: No on exercise 2 because you print the answer twice.  Yes on
#       exercise 3.
#   iii: Yes on exercise 2. No on exercise 3 because you haven't printed the
#       returned value.
#   iv: Yes on exercise 2. No on exercise 3 because you haven't printed the
#       returned value.
#   v: No on both exercises.  This equation is showing how to find the
#       area.  It's a boolean expression that would have the value 'true'
#
