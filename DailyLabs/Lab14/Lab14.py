# CS 210 - Introduction to Programming - Fall 2014
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains solutions to lab exercises. """

# Author is a constant for use in the program and by your instructor during grading.
AUTHOR = "\nNathan Ruprecht"

# A few constants for use in the Turtle Graphics problems.
WIDTH = 640             # Usually 640, 1024, or 1200
HEIGHT = WIDTH * 3 / 4  # Produces the eye-pleasing 4:3 ratio.
MARGIN = 20             # Somewhat arbitrary value, but it looks nice.

import sys
import urllib.error
import urllib.request


def main():
    """ Main program to test solutions for each exercise. """
    #exercise1()
    #exercise2()
    #exercise3()
    exercise4("http://dfcs/cs210/index.html")
    #exercise5()
    #exercise6()



######## Exercise 1 ########

def exercise1():
    """ Exercise 1 """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.
    myStr = []
    try:
        myStr[i] = 'E'
    except NameError:
        print("ERROR: You. Can't. Do. That.")
    


######## Exercise 2 ########

def exercise2():
    """ Exercise 2 """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.
    myStr = []
    try:
        myStr[i] = 'E'
    except NameError:
        print("ERROR: You. Can't. Do. That.")
    try:
        print(myStr[1000])
    except IndexError:
        print("ERROR: You're still doing something wrong.")


######## Exercise 3 ########

def exercise3():
    """ Exercise 3 """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.
    myStr = input("Give me the string:")
    assert(len(myStr) >= 30), "This program isn't going to work..."
    print(myStr[30])


######## Exercise 4 ########

def exercise4(url):
    """ Exercise 4 """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.
    try:
        return urllib.request.urlopen(url.read().decode()
    except urllib.error.URLError:
        print("ERROR: Could not find url {0}.".format(url),file=sys.stderr,flush=True)
    except:
        print("ERROR:Invalid url {0}.".format(url),file=sys.stderr,flush=True)
    return "" #Empty String

######## Exercise 5 ########

def exercise5():
    """ Exercise 5 """
    print( AUTHOR + exercise5.__doc__, flush=True )  # Leave this as the first line of the function.

    screen = turtle.Screen()
    screen.title( AUTHOR + exercise5.__doc__ )
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "LightSteelBlue" )

    # Define the turtle to be used for drawing (rename if you wish).
    teenage_mutant_ninja = turtle.Turtle()
    teenage_mutant_ninja.speed( "fast" )

    #### Insert your code/function calls BELOW here. ####



    #### Insert your code/function calls ABOVE here. ####

    screen.exitonclick()



######## Exercise 6 ########

def exercise6():
    """ Exercise 6 """
    print( AUTHOR + exercise6.__doc__, flush=True )  # Leave this as the first line of the function.

    screen = turtle.Screen()
    screen.title( AUTHOR + exercise6.__doc__ )
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "LightSteelBlue" )

    # Define the turtle to be used for drawing (rename if you wish).
    teenage_mutant_ninja = turtle.Turtle()
    teenage_mutant_ninja.speed( "fast" )

    #### Insert your code/function calls BELOW here. ####



    #### Insert your code/function calls ABOVE here. ####

    screen.exitonclick()


######## Main Program ########
if __name__ == "__main__":
    main()
