# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains _INSERT_DESCRIPTION_HERE_. """

# Put all import statements a the top of the file.
import turtle
import random
from random import randint

# Constant definitions go here, starting with your name.
AUTHOR = "C2C Nathan Ruprecht"

WIDTH = 640             # Usually 640, 1024, or 1200
HEIGHT = WIDTH * 3 / 4  # Produces the eye-pleasing 4:3 ratio.
MARGIN = 20             # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = 16          # Ditto
DRAW_FAST = True        # Set to False to see turtle in action.

NUM_BALLS = 9
SIZE = 32


######## Class Definitions Go Below Here ########

class  Ball:
    """ This class models a ball for the guided example in Lab 22. """

    number_of_balls = 9

    def __init__ (self, init_x = 0, init_y = 0):

        #Create attributes of a Ball object
        self.x = init_x
        self.y = init_x
        self.delta_x = randint(-1,1)
        self.delta_y = randint(-2,2)
        self.color = (random.random(), random.random(), random.random())
        self.size = randint(5, 150)

        Ball.number_of_balls += 1

        #Each Ball object gets its own turtle
        self.my_turtle = turtle.Turtle()
        self.my_turtle.penup()
        if DRAW_FAST:
            self.my_turtle.hideturtle()
            self.my_turtle.speed(2)

    def __str__(self):
        return "x={0}, y={1}, delta_x= {2}, delta_y={3}".format(self.x, self.y, self.delta_x, self.delta_y)


    def draw (self):
        """ Draw this ball object. """
        self.my_turtle.setposition (self.x, self.y)
        self.my_turtle.color(self.color)
        self.my_turtle.dot(self.size)

    def erase(self):
        """ Erase this ball object. """
        self.my_turtle.clear()

    def move(self):
        """ Updates the x and y coordinates of this Ball object, and
            checkto see if the ball objectneeds to turn around.
        """
        self.x += self.delta_x
        self.y += self.delta_y

        if self.x < (-WIDTH // 2) +(.5*self.size) or self.x > WIDTH//2 -(.5*self.size):
            self.delta_x *= -1

        if abs(self.y) > (HEIGHT // 2)-(.5*self.size):
            self.delta_y *= -1



######## Class Definitions Go Above Here ########



# Leave the main function in front of any other non-class functions.
def main():
    """ Main program to _INSERT_DESCRIPTION_HERE_. """

    # Set up the turtle graphics window first so the turtle.numinput dialogs
    # will appear offset from the turtle graphics window and look all pretty.
    screen = turtle.Screen()
    screen.title( AUTHOR )
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "LightSteelBlue" )

    # Make the animation display as fast as possible and turn off tracing.
    # Note: Once tracing is turned off, nothing actually draws until the
    # call to turtle.update() executes; this is called double-buffering.
    if DRAW_FAST:
        turtle.delay( 0 )
        turtle.tracer( 0 )

        
    ######## Main Program Code Goes Below Here ########

    ball = []

    for i in range(NUM_BALLS):
        i = Ball(randint(-WIDTH//3, WIDTH//3), randint(-HEIGHT//3,HEIGHT//3))
        ball.append(i)
        
    while True:
        for i in range(NUM_BALLS):
            ball[i].erase()
            ball[i].move()
            ball[i].draw()
    
        # If tracing is turned off, call update to show the drawing.
        # Note: For animatino, this statement must go inside the main
        # program loop, after all drawing for a given frame is complete.
        if DRAW_FAST:
            turtle.update()

    ######## Main Program Code Goes Above Here ########

    # Wait for the user to click before closing the window and exiting.
    screen.exitonclick()



######## Non-Class Function Definitions Go Below Here ########





######## Non-Class Function Definitions Go Above Here ########



######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
