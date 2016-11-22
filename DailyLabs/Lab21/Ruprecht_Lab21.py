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

class BankAccount:

    def __init__(self, customer):
        self.deposits = 0
        self.withdrawals = 0
        self.transfers = 0
        self.balance = 0

    def getdeposits(self):
        pass

    def getwithdrawals(self):
        pass

    def gettransfers(self):
        pass

    def getbalance(self):
        pass

    def setdeposits(self, amount):
        deposits += amount

    


def main():
    """ Main program to test solutions for each exercise. """
    #exercise1()
    exercise2()
    #exercise3()
    #exercise4()
    #exercise5()
    #exercise6()



######## Exercise 1 ########

def exercise1():
    """ Exercise 1 """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.

    ##Question 1 is the text file



######## Exercise 2 ########

def exercise2():
    """ Exercise 2 """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.

    c = BankAccount(Jim)


######## Exercise 3 ########

def exercise3():
    """ Exercise 3 """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.



######## Exercise 4 ########

def exercise4():
    """ Exercise 4 """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.




######## Exercise 5 ########

def exercise5():
    """ Exercise 5 """
    print( AUTHOR + exercise5.__doc__, flush=True )  # Leave this as the first line of the function.




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
