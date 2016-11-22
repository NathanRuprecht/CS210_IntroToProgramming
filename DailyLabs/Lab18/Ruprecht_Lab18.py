# CS 210 - Introduction to Programming - Fall 2014
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains solutions to lab exercises. """

import random

# Author is a constant for use in the program and by your instructor during grading.
AUTHOR = "\nNathan Ruprecht"

# A few constants for use in the Turtle Graphics problems.
WIDTH = 640             # Usually 640, 1024, or 1200
HEIGHT = WIDTH * 3 / 4  # Produces the eye-pleasing 4:3 ratio.
MARGIN = 20             # Somewhat arbitrary value, but it looks nice.



def main():
    """ Main program to test solutions for each exercise. """
    #exercise1()
    #matrix = exercise2()
    #exercise3(matrix)
    exercise4()
    #exercise5()
    #exercise6()



######## Exercise 1 ########

def exercise1():
    """ Exercise 1 """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.

    a_list = [37, 83, 42, 51, 99, 13, 29, 67]
    values = "Integrity first, Service before self, and Excellence in all we do."
    three = "Three Letter Acronym"

    part_a(a_list)
    print(part_b(a_list))
    print(part_c(values))
    print(part_d(values))

def part_a(alist):
    for i in range(len(alist)):
        print(alist[i])

def part_b(alist):
    blist = [num for num in alist if num%2==1]
    return blist

def part_c(values):
    wds = values.split()
    mylist = [len(item) for item in wds]
    return mylist

def part_d(three):
    thelist = three.split()
    init = ""
    if len(thelist) >= 3:
        for aname in thelist:
            init = init + aname[0]
    return init


######## Exercise 2 ########

def exercise2():
    """ Exercise 2 """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.

    matrix = rand_matrix(3, 4, 10, 99)
    matrix2 = rand_matrix(8, 6, 100, 999)
    print(matrix2)

    return matrix

def rand_matrix(row, column, minval, maxval):
    mylist = [[] for i in range(row)]
    

    for r in range(row):
        innerlist = [[] for i in range(column)]
        for c in range(column):
            innerlist[c] = random.randint(minval, maxval)
        mylist[r] = innerlist

    return mylist
        


######## Exercise 3 ########

def exercise3(matrix):
    """ Exercise 3 """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end="\t")
        print("\n")

######## Exercise 4 ########

def exercise4():
    """ Exercise 4 """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.

    a = [[1,2,3] [1,2,3]]
    b = [[1,2,3] [1,2,3]]
    add_matrix(a, b)

def add_matrix(a, b):
    c = [[] for i in range(len(a))]
    
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for r in range(len(a)):
            for c in range(len(a[0])):
                c[r][c] = a[r][c] + b[r][c]


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
