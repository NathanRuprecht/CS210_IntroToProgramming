# CS 210 - Introduction to Programming - Fall 2014
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains solutions to lab exercises. """

import random
import math

# Author is a constant for use in the program and by your instructor during grading.
AUTHOR = "\nNathan Ruprecht"

# A few constants for use in the Turtle Graphics problems.
WIDTH = 640             # Usually 640, 1024, or 1200
HEIGHT = WIDTH * 3 / 4  # Produces the eye-pleasing 4:3 ratio.
MARGIN = 20             # Somewhat arbitrary value, but it looks nice.



def main():
    """ Main program to test solutions for each exercise. """
    #exercise1()
    #exercise2()
    exercise3()
    #exercise4()
    #exercise5()
    #exercise6()



######## Exercise 1 ########

def exercise1():
    """ Exercise 1 """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.

    answer = get_midpoint(0,0,5,5)

    print(answer)

def get_midpoint(x1, y1, x2, y2):
    x3 = (x1+x2)/2
    y3 = (y1+y2)/2

    our_tuple = (x3, y3)

    return our_tuple



######## Exercise 2 ########

def exercise2():
    """ Exercise 2 """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.

    from Ruprecht_Lab16 import rand_list

    a_set = set( rand_list( 5, 10, 99))
    b_set = set( rand_list( 5, 10, 99))
    print("a_set:", a_set)
    print("b_set:", b_set)
    
    print("Union:", set.union(a_set, b_set))
    print("Intersection:", set.intersection(a_set, b_set))
    print("Difference:", set.difference(a_set, b_set))
    print("Symmetric difference:", set.symmetric_difference(a_set, b_set))
    


######## Exercise 3 ########

def exercise3():
    """ Exercise 3 """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.

    from timeit import timeit
    timeit("iter_test(iterable)", setup="from_main_import iter_test; iterable = set(range(10000))",number=100000)
    timeit("iter_test(iterable)",setup="from __main__ import iter_test; iterable = list(range(10000))",number=100000)
    timeit("iter_test(iterable)",setup="from __main__ import iter_test; iterable = tuple(range(10000))",number=100000)

def iter_test(iterable):
    for i in iterable:
        pass
    


######## Exercise 4 ########

def exercise4():
    """ Exercise 4 """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.




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
