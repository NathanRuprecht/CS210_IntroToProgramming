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





######## Class Definitions Go Above Here ########



# Leave the main function in front of any other non-class functions.
def main():
    with open('myPickledDictionary.pickle', 'rb') as f:
        dictionary = pickle.load(f)

    print(dictionary)

    with open('myPickledList.pickle', 'rb') as f:
        mylist = pickle.load(f)

    print(mylist)

    with open('myPickledPointsList.pickle', 'rb') as f:
        pointslist = pickle.load(f)

    print(pointslist)



######## Non-Class Function Definitions Go Below Here ########





######## Non-Class Function Definitions Go Above Here ########



######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
