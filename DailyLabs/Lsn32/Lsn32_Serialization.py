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
import random
import pickle

# Constant definitions go here, starting with your name.
AUTHOR = "C2C Nathan Ruprecht"



######## Class Definitions Go Below Here ########

class Point:

    def __init__( self ):
        self.x = 0
        self.y = 0

    def __str__( self ):
        return "x=" + str( self.x ) + "y=" + str( self.y )

    def setXY( self, x, y ):
        self.x = x
        self.y = y

    def Add( self, pointToAddx, pointToAddy ):
        setXY( (x+pointToAddx) , (y+pointToAddy) )




######## Class Definitions Go Above Here ########



# Leave the main function in front of any other non-class functions.
def main():

    point = exercise1()
    exercise3(point)
    exercise7()

def exercise1():
    point = {}
    point['x'] = 1
    point['y'] = 2

    with open('myPickledDictionary.pickle', 'wb') as f:
        pickle.dump(point, f)

    return (point)



def exercise3(point):

    point_copy = point.copy()
    point_copy['x'] = 8
    point_copy['y'] = 9

    myList = [[] for i in range(2)]
    myList[0] = point
    myList[1] = point_copy               

    with open('myPickledList.pickle', 'wb') as f:
        pickle.dump(myList, f)


def exercise7():
    point={}
    
    for i in range(1, 10):
        point[i] = Point()
        #Point.setXY(random.randint(-100, 100) , random.randint(-100, 100))

    with open('myPickledPointsList.pickle', 'wb') as f:
        pickle.dump(point, f)

    
######## Non-Class Function Definitions Go Below Here ########





######## Non-Class Function Definitions Go Above Here ########



######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
