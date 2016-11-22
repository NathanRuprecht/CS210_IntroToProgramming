# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#


import turtle
import math


WIDTH = 640             # Usually 640, 1024, or 1200
HEIGHT = WIDTH * 3 / 4  # Produces the eye-pleasing 4:3 ratio.

MARGIN = 20             # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = 9          # Ditto

DRAW_FAST = True        # Set to False to see turtle in action.



def main():
    """ Main program to satisfy requirements of PEX01 """

    # Set up the turtle graphics window first so the turtle.numinput dialogs
    # will appear offset from the turtle graphics window and look all pretty.
    screen = turtle.Screen()
    screen.title( "C2C Nathan Ruprecht" )
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "white" )

    # Make the animation display as fast as possible and turn off tracing.
    if DRAW_FAST:
        turtle.delay( 0 )
        turtle.tracer( 0 )

    # Create a turtle to do the drawing, making it stealthy and fast.
    jim = turtle.Turtle()
    if DRAW_FAST:
        jim.hideturtle()
        jim.speed( 0 )

    #Get the number of cylinders to be drawn
    tanks = number_of_tanks()

    #Go through a loop to draw all the cylinders
    for i in range(tanks):
        cylinder_height = overall_height()
        RADIUS = overall_radius(cylinder_height)
        LIQUID_H = liquid_height(cylinder_height)

        #Calculate volume depending on where the water level is
        if (LIQUID_H < RADIUS):
            volume = (1/3) * (math.pi) * (LIQUID_H ** 2) *(3 * RADIUS - LIQUID_H)
        if (LIQUID_H > RADIUS and LIQUID_H < (cylinder_height - RADIUS)):
              volume = (2/3)*(math.pi)*(RADIUS**3)+(math.pi * RADIUS**2)*(LIQUID_H - RADIUS)
        if(LIQUID_H > (cylinder_height - RADIUS)):
              volume = (4/3 * math.pi * RADIUS**3)+((math.pi*RADIUS**2)*(cylinder_height - 2*RADIUS))-((1/3 * math.pi *((LIQUID_H - cylinder_height)**2)*(3*RADIUS - LIQUID_H + cylinder_height)))
          

        #Scaling the radius to be drawn
        draw_radius = (RADIUS / cylinder_height) * HEIGHT
        
        #reset everything to draw next cylinder
        jim.penup()
        jim.home()
        jim.pendown()
        turtle.resetscreen()
        turtle.resetscreen()

        #Function to actually draw the cylinder
        draw_cylinder(jim, RADIUS, HEIGHT, draw_radius, LIQUID_H, cylinder_height, volume)

        #Draw the info in the upper left corner
        write_H(jim, WIDTH, HEIGHT, FONT_SIZE, cylinder_height)
        write_r(jim, WIDTH, HEIGHT, FONT_SIZE, RADIUS)
        write_h(jim, WIDTH, HEIGHT, FONT_SIZE, LIQUID_H)


    # If tracing is turned off, call update to show the drawing.
    if DRAW_FAST:
        turtle.update()

    # Wait for the user to click before closing the window and exiting.
    screen.exitonclick()







def write_H(jim, WIDTH, HEIGHT, FONT_SIZE, cylinder_height):
    """Write "H" in the upper left corner"""
    
    jim.penup()
    
    #Put the turtle in place in the upper left
    jim.setposition( -(.45 * WIDTH), HEIGHT // 2 - FONT_SIZE * 2 )
    jim.pendown()

    #Write the H=
    jim.write( "H = ", move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
    jim.penup()
    jim.setposition( -(.45 * WIDTH) + 25, HEIGHT // 2 - FONT_SIZE * 2 )
    jim.pendown()

    #Write the value for H
    jim.write(cylinder_height, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )


def write_r(jim, WIDTH, HEIGHT, FONT_SIZE, RADIUS): 
    """Write "r" in the upper left corner"""

    jim.penup()

    #Put the turtle in place below the H=
    jim.setposition( -(.45 * WIDTH), HEIGHT // 2 - FONT_SIZE * 3.5 )
    jim.pendown()

    #Write the r=
    jim.write( "r = ", move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
    jim.penup()
    jim.setposition( -(.45 * WIDTH) + 25, HEIGHT // 2 - FONT_SIZE * 3.5 )
    jim.pendown()

    #Write the value for r
    jim.write(RADIUS, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )


def write_h(jim, WIDTH, HEIGHT, FONT_SIZE, LIQUID_H):
    """Write "h" in the upper left corner"""
    
    jim.penup()

    #Put the turtle below the r=
    jim.setposition( -(.45 * WIDTH), HEIGHT // 2 - FONT_SIZE * 5 )
    jim.pendown()

    #Write h= 
    jim.write( "h = ", move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
    jim.penup()
    jim.setposition( -(.45 * WIDTH) + 25, HEIGHT // 2 - FONT_SIZE * 5 )
    jim.pendown()
    
    #Write the value for h
    jim.write(LIQUID_H, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )


def draw_cylinder(jim, RADIUS, HEIGHT, draw_radius, LIQUID_H, cylinder_height, volume):
    """Jim draws cylinder"""

    #Draw the dashed line if the water level is between semicricles
    if (LIQUID_H > RADIUS and LIQUID_H < (cylinder_height - RADIUS)):
        
        #Save the coordinates of jim before drawing the dashed line
        x = jim.xcor()
        y = jim.ycor()
        jim.left(180)
        jim.penup()
        jim.forward(draw_radius)
        jim.left(180)
        
        #Actually draw the dashed line
        for i in range(0, int(draw_radius), 5):
            jim.forward(5)
            jim.penup()
            jim.forward(5)
            jim.pendown()
        jim.penup()

        #Put jim in place to write V=
        jim.setposition(0, y + 15)
        jim.pendown()

        #Write V=
        jim.write("V =", move=False, align="center",
                  font=("Courier", FONT_SIZE, "bold"))
        jim.penup()
        jim.setposition( 0, y)
        jim.pendown()
        
        #Write the volume above dashed line
        jim.write( volume, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
        jim.penup

        #Return jim to place before dashed line
        jim.setx(x)
        jim.sety(y)

    #Draw straight line along right side of cylinder
    jim.penup()
    jim.forward(draw_radius)
    jim.left(90)
    jim.pendown()
    jim.forward((HEIGHT / 2) - draw_radius - 15)

    #Draw the dashed line if the water level is in the upper semicircle
    if(LIQUID_H > (cylinder_height - RADIUS)):

        #Save the coordinates of jim before drawing the dashed line
        x = jim.xcor()
        y = jim.ycor()

        jim.left(90)

        #Actually draw the dashed line
        for i in range(0, int(draw_radius), 5):
            jim.forward(5)
            jim.penup()
            jim.forward(5)
            jim.pendown()
        jim.penup()

        #Return jim to place before dashed line
        jim.setx(x)
        jim.sety(y)

        jim.right(90)
        jim.penup()

        #Put jim in place to write V=
        jim.setposition(0, y + 15)
        jim.pendown()

        #Write V=
        jim.write("V =", move=False, align="center",
                  font=("Courier", FONT_SIZE, "bold"))
        jim.penup()

        #Put jim in place to write the volume
        jim.setposition( 0, y)
        jim.pendown()

        #Write the volume
        jim.write( volume, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
        jim.penup()

        #Return jim to place before dashed line
        jim.setx(x)
        jim.sety(y)
    jim.pendown()

    #Draw upper semicircle of cylinder
    jim.circle(draw_radius, 180)

    #Draw left side of cylinder
    jim.forward((HEIGHT - (2 * draw_radius)) -30)

    #Drawing dashed line if water level is in lower semicircle of cylinder
    if (LIQUID_H < RADIUS):

        #Save coordinates before drawing the dashed line
        x = jim.xcor()
        y = jim.ycor()

        jim.left(90)

        #Actually draw the dashed line
        for i in range(0, int(draw_radius), 5):
            jim.forward(5)
            jim.penup()
            jim.forward(5)
            jim.pendown()

        jim.setx(x)
        jim.sety(y)

        jim.right(90)
        jim.penup()

        #Put jim in place to write V=
        jim.setposition(0, y + 15)
        jim.pendown()

        #Write V=
        jim.write("V =", move=False, align="center",
                  font=("Courier", FONT_SIZE, "bold"))
        jim.penup()
        
        #Put jim in place to write volume above dashed line
        jim.setposition( 0, y)
        jim.pendown()

        #Write the volume above the dashed line
        jim.write( volume, move=False, align="center",
               font=( "Courier", FONT_SIZE, "bold" ) )
        jim.penup()

        #Return jim to place before drawing the dashed line
        jim.setx(x)
        jim.sety(y)
    jim.pendown()

    #Draw lower semicircle of cylinder
    jim.circle(draw_radius, 180)

    #Complete cylinder by drawing last half of right side
    jim.forward((HEIGHT / 2) - draw_radius - 15)


def number_of_tanks():
    """Get the number of cylinders to be drawn"""
    
    tanks = int(turtle.numinput("Number of tanks", "How many tanks do you want to specify?",
               0, minval=1, maxval=10))
    while (tanks < 1 or tanks >10):
        tanks = int(turtle.numinput("ERROR: INVALID INPUT", "How many tanks do you want to specify?",
               0, minval=1, maxval=10))
    
    return tanks

        
def overall_height():
    """Get the height of the cylinder"""
    
    cylinder_height = turtle.numinput("Overall height", "What is the overall height?",
               0, minval=3, maxval=100)
    while(cylinder_height < 3 or cylinder_height > 100):
        cylinder_height = turtle.numinput("ERROR: INVALID INPUT", "What is the overall height?",
               0, minval=3, maxval=100)
    
    return cylinder_height


def overall_radius(cylinder_height):
    """Get the radius of the cylinder"""
    
    max_value = (cylinder_height/3)
    
    RADIUS = turtle.numinput("Radius", "What is the radius of the cylinder?", 0, minval = 1,
                             maxval=max_value)
    while(RADIUS < 1 or RADIUS > max_value):
        RADIUS = turtle.numinput("ERROR: INVALID INPUT", "What is the radius of the cylinder?", 0,
                                 minval = 1,maxval=max_value)

    return RADIUS


def liquid_height(cylinder_height):
    """Get the height of the liquid in the cylinder"""
    
    LIQUID_H = turtle.numinput("Liquid Height", "What is the height of the liquid?", 0, minval = 0,
                             maxval=cylinder_height)
    while(LIQUID_H < 0 or LIQUID_H > cylinder_height):
        LIQUID_H = turtle.numinput("ERROR: INVALID INPUT", "What is the height of the liquid?", 0,
                                   minval = 0,maxval=cylinder_height)

    return LIQUID_H

    


######## Main program ########
if __name__ == "__main__":
    main()
