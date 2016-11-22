# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains examples of recursive drawing functions. """

# Put all import statements a the top of the file.
import random
import turtle
import time
import sys

# Constant definitions go here, starting with your name.
AUTHOR = "C2C Nathan Ruprecht"

##########################################################################
# NOTE: The main() function, remaining constant definitions, and various #
# other utility functions have been moved to the bottom of this file     #
# because YOU DO NOT NEED TO EDIT ANY OF THIS CODE. Your work will be    #
# done in the recursive functions immediately following this comment.    #
##########################################################################

######## Sierpinski Triangle ########

def draw_sierpinski_triangle( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # http://en.wikipedia.org/wiki/Sierpinski_triangle

    # Build the first, largest triangle to get started, creating points
    # as tuples with two integer values (x,y) and a triangle as a tuple
    # of three points.
    top = ( 0, HEIGHT//2 - MARGIN )
    left = ( -WIDTH//2 + MARGIN, -HEIGHT//2 + MARGIN )
    right = (  WIDTH//2 - MARGIN, -HEIGHT//2 + MARGIN )
    triangle = ( top, left, right )

    # Draw a single large triangle filling the entire window.
    tom.color( "Blue" )
    fill_triangle( tom, triangle )

    # The Sierpinski Triangle pattern is now achieved by recursively
    # erasing inner triangles.  NOTE: The version in the book avoids
    # this by drawing each size of triangles in a different color.
    tom.color( "White" )

    # Start the recursion with the initial triangle and depth=3.
    sierpinski_triangle( tom, triangle, 7 )

def sierpinski_triangle( tom, triangle, depth ):
    """ Uses the given turtle to draw the Sierpinski Triangle pattern within the given triangle. """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Nothing to do in the base case, so test the condition to keep going.
    # Specifically, if the points of the triangle are sufficiently far apart.
    if depth > 0 and distance_between( triangle[ 0 ], triangle[ 1 ] ) > 4:
        # "Unpack" the points from the triangle tuple.
        top, left, right = triangle

        # Find the midpoint of each side of the triangle.
        left_mid = midpoint( left, top )
        right_mid = midpoint( right, top )
        bottom_mid = midpoint( left, right )

        # Fill (i.e., erase since tom is drawing in white) the inner triangle.
        fill_triangle( tom, ( bottom_mid, left_mid, right_mid ) )

        # Recursively draw the same pattern in each of the smaller triangles.
        # Note the last parameter decreases depth by one in each recursive call.

        # TODO 1a: Un-comment the line below to draw the pattern inside the
        #          top triangle. Run the program and observe the result.
        sierpinski_triangle( tom, ( top, left_mid, right_mid ), depth - 1 )

        # TODO 1b: Un-comment the line below to draw the pattern inside the
        #          left triangle. Run the program and observe the result.
        sierpinski_triangle( tom, ( left_mid, left, bottom_mid ), depth - 1 )

        # TODO 1c: Un-comment the line below to draw the pattern inside the
        #          left triangle. Run the program and observe the result.
        sierpinski_triangle( tom, ( right_mid, bottom_mid, right ), depth - 1 )

        # TODO 1d: Rearrange the order of the above three lines of code
        #          and re-run the program to observe the results.

        # TODO 1e: The last line (52) of the draw_sierpinski_triangle() function
        #          calls the recursive sierpinski_triangle() function with the
        #          last parameter of 3 indicating the depth of the recursion.
        #          Change this value to 4 and re-run the program. Change it to 5
        #          and run the program again. Do you have the patience to try 6
        #          or 7? If you do and want to stop, press Escape to see the menu.


def distance_between( p1, p2 ):
    """ Calculate and return the distance between two points (stored as (x,y) tuples). """
    # "Unpack" the point tuples into x,y coordinates.
    x1, y1 = p1
    x2, y2 = p2
    # Calculate and return the distance between the two points.
    return ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 ) ** 0.5

def midpoint( p1, p2 ):
    """ Create and return the midpoint between two points (stored as (x,y) tuples). """
    # "Unpack" the point tuples into x,y coordinates.
    x1, y1 = p1
    x2, y2 = p2
    # Calculate and return the midpoint as a new (x,y) tuple.
    return ( ( x1 + x2 ) / 2, ( y1 + y2 ) / 2 )

def fill_triangle( tom, points ):
    """ Uses the given turtle to fill a triangle with the given points. """
    # Lift the pen and move to the first point in the triangle.
    tom.penup()
    tom.setposition( points[ 0 ] )
    tom.pendown()
    # Begin filling and move to the second and third points,
    # and then back to the first point to close the triangle.
    tom.begin_fill()
    tom.setposition( points[ 1 ] )
    tom.setposition( points[ 2 ] )
    tom.setposition( points[ 0 ] )
    tom.end_fill()


######## Sierpinski Carpet ########

def draw_sierpinski_carpet( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # http://en.wikipedia.org/wiki/Sierpinski_carpet

    # No need to position tom or draw anything before getting started,
    # so just call the recursive function with the center and size of
    # the entire carpet and the recursive depth=3.
    sierpinski_carpet( tom, 0, 0, WIDTH, HEIGHT, 5 )

def sierpinski_carpet( tom, center_x, center_y, width, height, depth ):
    """ Uses the given turtle to draw the Sierpinski Carpet.
        http://en.wikipedia.org/wiki/Sierpinski_carpet
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Nothing to do in the base case, so test the condition to keep going.
    # Specifically, if the piece of carpet is large enough to split.
    if depth > 0 and min( width, height ) > 3:
        # Temporary variables to hold the width and height of each of the
        # nine smaller sub-carpets that need to be drawn.
        w = width // 3
        h = height // 3

        # Fill the center sub-carpet.
        fill_rect( tom, center_x, center_y, w, h )

        # Recursively draw the pattern in each of the other eight sub-carpets.
        sierpinski_carpet( tom, center_x + w, center_y + h, w, h, depth - 1 )

        # TODO 2a: Make a copy of the above line and change the additions
        #          to subtractions. Run the program and observe the result.
        sierpinski_carpet( tom, center_x - w, center_y - h, w, h, depth - 1 )


        # TODO 2b: Make six more copies of the above line, ONE AT A TIME, for each
        #          of the remaining directions in the pattern. That is, there will
        #          be one that does -w and +h, one that does +w and -h, one that
        #          only does +w, one that only does -w, one that only does +h,
        #          and one that only does -h. Run the program after adding each
        #          individual line and observe the result.
        sierpinski_carpet( tom, center_x - w, center_y + h, w, h, depth - 1 )
        sierpinski_carpet( tom, center_x + w, center_y - h, w, h, depth - 1 )
        sierpinski_carpet( tom, center_x, center_y - h, w, h, depth - 1 )
        sierpinski_carpet( tom, center_x, center_y + h, w, h, depth - 1 )
        sierpinski_carpet( tom, center_x - w, center_y, w, h, depth - 1 )
        sierpinski_carpet( tom, center_x + w, center_y, w, h, depth - 1 )


        # TODO 2c: Rearrange the above recursive calls so the pattern fills starting
        # with the upper-right and moving clockwise. That is, if the pattern were the
        # numbers on a telephone and the center square were the 5, it would fill the
        # following squares in the order 3, 6, 9, 8, 7, 4, 1, 2.

        # TODO 2d: Change the initial depth of the recursion and re-run the program.


def fill_rect( tom, x, y, w, h ):
    """ Uses the given turtle to fill a rectangle centered at (x,y). """
    # Lift the pen and move to a corner of the rectangle.
    tom.penup()
    tom.setposition( x - w // 2, y + h // 2 )
    tom.pendown()
    # Draw a filled rectangle.
    tom.begin_fill()
    for side in range( 2 ):
        tom.forward( w )
        tom.right( 90 )
        tom.forward( h )
        tom.right( 90 )
    tom.end_fill()



######## Sierpinski-ish Circles ########

def draw_sierpinski_circles( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # No need to position tom or draw anything before getting started,
    # so just call the recursive function with the center and size of
    # the initial circle and the recursive depth=3.
    sierpinski_circles( tom, 0, 0, ( WIDTH + HEIGHT ) // 8, 5 )

def sierpinski_circles( tom, center_x, center_y, radius, depth ):
    """ Uses the given turtle to draw filled circles in a Sierpinski-ish pattern. """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # If the circle size is large enough, keep going.
    if depth > 0 and radius > 1:
        # Move the turtle to the center of the circle and draw a dot.
        tom.setposition( center_x, center_y )
        tom.dot( radius * 2 )

        # Recursively draw smaller circles in each diagonal direction.
        sierpinski_circles( tom, center_x - radius, center_y + radius, radius // 2, depth - 1 )

        # TODO 3a: Make three copies of the above line for each of the other diagonal directions.
        #          This is very similar to the carpet pattern, but it only moves diagonally.
        sierpinski_circles( tom, center_x + radius, center_y + radius, radius // 2, depth - 1 )
        sierpinski_circles( tom, center_x - radius, center_y - radius, radius // 2, depth - 1 )
        sierpinski_circles( tom, center_x + radius, center_y - radius, radius // 2, depth - 1 )


        # TODO 3b: Arrange your recursive calls so the pattern draws counter-clockwise.


        # TODO 3c: Move the three lines of code from above that draw the dot
        #          (ok, two lines of code and one comment) so they are BELOW
        #          the recursive calls. Run the program and observe the result.

        # TODO 3d: Change the initial depth of the recursion and re-run the program.


######## H-Tree ########

def draw_h_tree( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # No need to position tom or draw anything before getting started,
    # so just call the recursive function with the center and size of
    # the initial H and the recursive depth=3.
    h_tree( tom, 0, 0, ( WIDTH + HEIGHT ) // 4, 6 )

def h_tree( tom, center_x, center_y, size, depth ):
    """ Recursively draws an H-tree. """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # If the H size is large enough, keep going.
    if depth > 0 and size > 4:
        # Draw the center horizontal line.
        draw_line( tom, center_x - size//2, center_y, center_x + size//2, center_y )
        # Draw the left vertical line.
        draw_line( tom, center_x - size//2, center_y - size//2, center_x - size//2, center_y + size//2 )
        # Draw the right vertical line.
        draw_line( tom, center_x + size//2, center_y - size//2, center_x + size//2, center_y + size//2 )

        # Recursively draw a smaller H in each direction.

        # TODO 4a: This time none of the recursive calls are provided, so you must
        #          write all four. Don't panic ... they are very similar to the circles
        #          in the previous problem. The size of each H is decreased by half
        #          and the center point of each H is either increased or decreased
        #          by half of the size. Run the program after adding each individual
        #          recursive call and observe the result.
        h_tree( tom, center_x + size//2, center_y - size//2, size//2, depth - 1 )
        h_tree( tom, center_x - size//2, center_y + size//2, size//2, depth - 1 )
        h_tree( tom, center_x - size//2, center_y - size//2, size//2, depth - 1 )
        h_tree( tom, center_x + size//2, center_y + size//2, size//2, depth - 1 )

        # TODO 4b: Move the six lines of code from above that draw the lines (ok,
        #          three lines of code and three comments) so they are BELOW the
        #          recursive calls. Run the program and observe the result.


        # TODO 4c: Move the two lines of code that draw the center horizontal line
        #          back above the recursive calls. Run the program.


        # TODO 4d: Change the initial depth of the recursion and re-run the program.



def draw_line( tom, x1, y1, x2, y2 ):
   """ Draws a line between the two given points using the given turtle. """
   tom.penup()
   tom.setposition( x1, y1 )
   tom.pendown()
   tom.setposition( x2, y2 )


######## Leafy Tree ########

FALL_COLORS = [ "Red", "Orange", "OrangeRed", "Purple", "Orchid", "ForestGreen", "SandyBrown" ]

def draw_leafy_tree( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # Center the turtle horizontally, toward the bottom of the screen.
    tom.penup()
    tom.setposition( 0, -HEIGHT//3 )
    tom.pendown()
    tom.setheading( 90 )  # Straight up.
    tom.color( "Brown" )  # The tree trunk and branches are brown.
    # Start the recursion with the initial branch length and depth=3.
    leafy_tree( tom, HEIGHT//5, 5 )

def leafy_tree( tom, branch_length, depth ):
    """ Recursively draws a fruit tree. """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Finally, there is something to do in the base case ... draw a leaf!
    if depth <= 0 or branch_length < 4:
        # TODO 5c: Note ... do this last, after completing 5a and 5b below ...
        #          Draw a leaf using tom.dot() with a random pixel size between
        #          4 and 8 pixels. Also, use random.choice() to get a random
        #          color from the list of FALL_COLORS defined above.
        #          Remember to set the color back to Brown after drawing the leaf!
        pass

    else:
        # Use the recursion depth as the circumference of the branch
        # (i.e., turtle pensize), so the branches are thinner near the end.
        tom.pensize( depth )
        tom.forward( branch_length )

        # Turn slightly to the right and recursively draw a smaller tree.
        tom.right( 30 )
        leafy_tree( tom, branch_length * 3 // 4, depth - 1 )

        # TODO 5a: Copy the two lines above and change the right( 30 )
        #          to left( 60 ) so the left smaller tree will be 30
        #          degrees to the left.
        #          Next, add two more lines of code that turn the turtle
        #          right( 30 ) so it is pointing straight up again and
        #          then move the turtle backward the branch length so
        #          it is back in its original position.
        #          Run the program and observe the results.
        #          How did adding a recursive call with a LEFT turn end
        #          up drawing so many more RIGHT branches as well? Fun!
        tom.left( 60 )
        leafy_tree( tom, branch_length * 3 // 4, depth - 1 )
        tom.right( 30 )
        tom.backward( branch_length )


        # TODO 5b: The above modifications draw a very balanced tree. The
        #          images in the lab document show a more natural looking
        #          tree drawn by turning left 80 degrees and drawing the
        #          smaller tree with a branch size one-third smaller.
        #          Make these modifications to your code.
        #          NOTE: However far left you turn your turtle, you must
        #          turn it back right enough to point straight up.


        # TODO 5d: Change the initial depth of the recursion and re-run the program.



######## Koch Snowflake ########

def draw_koch_snowflake( tom ):
    """ Position the turtle, if necessary, and start the recursion. """
    # The size of the snowflake to fill about two-thirds of the screen.
    size = min( WIDTH, HEIGHT ) * 2 // 3
    # Center the turtle horizontally, at the top tip of the snowflake,
    # which is above the center by about 60% of the size of the snowflake.
    tom.penup()
    tom.setposition( 0, size * 3 // 5 )
    tom.pendown()
    # Facing down the side of the first equilateral triangle.
    tom.setheading( 300 )
    # Start the recursion with the length of the side of the
    # triangle and the recursion depth=3.
    koch_snowflake( tom, size, 4 )

def koch_snowflake( tom, size, depth ):
    """ Uses a loop to draw the three sides of the snowflake. (Yes, a loop.) """
    for side in range( 3 ):
        snowflake_side( tom, size, depth )
        tom.right( 120 )

def snowflake_side( tom, length, depth ):
    """ Recursively draws one side of the snowflake. """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # TODO 6: Complete the code below to draw the Koch Snowflake.
    #         Drawing a single straight line is the correct action in the base case.
    #         Replace the True in the if-statement with an appropriate condition that
    #         tests both the depth and length variables.
    #         Then, replace the pass statement in the else clause with appropriate
    #         recursive calls and turns to draw the rest of the snowflake.
    #         There will be four recursive calls since each straight edge of a
    #         larger triangle is divided into four pieces. The length of each
    #         of these smaller edges will be one-third of the current length.
    #         Also, don't forget to subtract one from the depth variable in
    #         each recursive call. Finally, recall the inner angles of an
    #         equilateral triangle are sixty degrees.
    if depth >= 0:
        tom.forward( length )
    else:
        knoch_snowflake( tom, length, depth - 1 )
        



########################################################
######## DO NOT CHANGE ANY CODE BELOW THIS LINE ########
########################################################

# NOTE: See note at top of file about why these constants are down here.
WIDTH = 640             # Usually 640, 800, 1024, or 1200
HEIGHT = WIDTH          # A square window for this applicaiton.
MARGIN = 20             # Somewhat arbitrary value, but it looks nice.

DRAW_FAST = True       # Set to False to see turtle in action.

# The following constants are used by show_menu() and menu_click().
OPTIONS = [ "Sierpinski Triangle", "Sierpinski Carpet", "Sierpinski-ish Circles",
            "H Tree", "Leafy Tree", "Koch Snowflake", "Exit" ]
FONT_SIZE = HEIGHT // 4 // len( OPTIONS )
BUTTON_SIZE = FONT_SIZE * 4


# NOTE: See note at top of file about why this function is down here.
def main():
    """ Main program to show menu of recursive drawing functions. """

    # Set up the turtle graphics window first so the turtle.numinput dialogs
    # will appear offset from the turtle graphics window and look all pretty.
    screen = turtle.Screen()
    screen.title( AUTHOR + "'s Recursion" )
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "White" )

    # Make the animation display as fast as possible and turn off tracing.
    # Note: Once tracing is turned off, nothing actually draws until the
    # call to turtle.update() executes; this is called double-buffering.
    if DRAW_FAST:
        turtle.delay( 0 )
        turtle.tracer( 0 )

    # Create a turtle to do the drawing, making it stealthy and fast.
    tom = turtle.Turtle()
    tom.hideturtle()
    tom.speed( 0 )
    tom.color( "Blue" )

    ######## Main Program Code Goes Below Here ########

    show_menu( tom )

    # Tell the system to call menu_click when the turtle screen is clicked.
    screen.onclick( menu_click )

    # Tell the system to call key_press when the Escape key is pressed
    # and then start listening for key presses.
    screen.onkey( key_press, key="Escape" )
    screen.listen()

    # Start the main loop that listens for mouse clicks and key presses.
    screen.mainloop()

    ######## Main Program Code Goes Above Here ########

    # This is normally the last line of a Python Turtle program, but waiting
    # for mouse clicks requires the above mainloop() call to be last.
    # Wait for the user to click before closing the window and exiting.
    # screen.exitonclick()


def key_press():
    """ Called by the system when the user presses the Escape key. """
    # Use a function attribute to indicate a key has been pressed.
    # For more on function attributes: http://legacy.python.org/dev/peps/pep-0232/
    key_press.escape = True


def show_menu( tom ):
    """ Show a menu of options, spaced nicely on the screen. """
    # Clear everything tom has drawn and move to the top, center of the window.
    tom.clear()
    tom.penup()
    tom.color( "Blue" )
    tom.setposition( 0, HEIGHT // 2 - BUTTON_SIZE * 3 // 4 )
    tom.setheading( 270 )  # Straight down.
    for option in OPTIONS:
        tom.write( option, align="center", move=False, font=( "Courier", FONT_SIZE, "bold" ) )
        tom.forward( BUTTON_SIZE )  # Move down to the next button location.

    if DRAW_FAST:  # If tracing is turned off, call update to show the menu.
        turtle.update()

    # See the note about function attributes in the key_press() function.
    key_press.escape = False


def menu_click( x, y ):
    """ Figures out which 'button' was pressed and draws the appropriate image. """
    # The turtle screen is a "Singleton Object", which means there is only one.
    # When this line of code is called in main(), it creates the new screen.
    # When this line of code is called here, it gets the already created screen.
    screen = turtle.Screen()

    # Don't listen for more clicks while drawing the current shape.
    screen.onclick( None )

    # Shift and invert the y-coordinate so it is a positive number with 0 at the top of the screen.
    # This way, when divided by BUTTON_SIZE, it can be used as an index into the OPTIONS list.
    y = HEIGHT - ( y + HEIGHT // 2 )
    option = OPTIONS[ int( y / BUTTON_SIZE ) ]

    # Since this function can only receive two parameters from the system,
    # we have to get our faithful turtle, tom, from the list of all turtles.
    tom = turtle.turtles()[ 0 ]  # First in the list since there is only one.
    tom.clear()
    tom.penup()
    tom.home()
    tom.pensize( 1 )

    # Figure out which shape is being requested and draw it.
    if option == "Sierpinski Triangle":
        draw_sierpinski_triangle( tom )
    elif option == "Sierpinski Carpet":
        draw_sierpinski_carpet( tom )
    elif option == "Sierpinski-ish Circles":
        draw_sierpinski_circles( tom )
    elif option == "H Tree":
        draw_h_tree( tom )
    elif option == "Leafy Tree":
        draw_leafy_tree( tom )
    elif option == "Koch Snowflake":
        draw_koch_snowflake( tom )
    else:
        turtle.bye()  # Closes the turtle screen.
        sys.exit()    # Actually stops the program.

    if DRAW_FAST:  # If tracing is turned off, call update to show the image drawn.
        turtle.update()

    # Pause for a few seconds to admire the pretty picture, then show the menu again.
    # (Skip the pause of the user impatiently presses the Escape key.)
    if not key_press.escape:
        time.sleep( 3 )
    show_menu( tom )

    # Start listening for clicks again.
    screen.onclick( menu_click )


######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
