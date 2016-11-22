# CS 210 - Introduction to Programming - Fall 2014
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#
# Author is a constant for use in the program and by your instructor during grading.

AUTHOR = "C2C Nathan Ruprecht"

""" This file contains solutions for Lab 12, String Basics. """


def main():
    """ Main program to test solutions for each exercise. """
    stuff = exercise1()
    #stuff = exercise2(stuff)
    #exercise3(stuff)
    #exercise4(stuff)
    exercise5(stuff)
    #exercise6()



######## Exercise 1 ########

def exercise1():
    """ Create a Python program that inputs a string from the user. Once the string
        is obtained print the string back to the screen one character per line.
    """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.

    string = input("Enter some stuff:")
    print(string, "\n")
    return string


######## Exercise 2 ########

def exercise2(stuff):
    """ Using the string obtained in Q1 convert the sting to all uppercase letters and print it to the screen. """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.

    print(stuff.upper(), "\n")
    return stuff


######## Exercise 3 ########

def exercise3(stuff):
    """ Convert the string back to lowercase letters and print it a random number of times using one 'print' statement and no loops. """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.

    print(stuff.lower(), "\n")


######## Exercise 4 ########

def exercise4(stuff):
    """ Using one line of code determine how many times the character ‘e’ appears in your string.
        Print the number to the screen. Replace all the ‘e’ characters with ‘E’ characters and print the string.
    """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.

    print(stuff.count("e"), "\n")


######## Exercise 5 ########

def exercise5(stuff):
    """ Strings in python are immutable. To demonstrate, create a program that takes a string
        from the user then modify the second character directly (i.e. myStr[1]=’d’).
        What was the result? What does immutable mean?
    """
    print( AUTHOR + exercise5.__doc__, flush=True )  # Leave this as the first line of the function.

    print(stuff.replace(stuff[1], "N"))


######## Exercise 6 ########

def exercise6():
    """ Create a program that asks a user for two inputs, their first name and their last name.
        Once obtained validate the input is a string of characters (‘a’/’A’-‘z’/’Z’).
        Ensure there are no extraneous white space and that each name is properly capitalized.
        Finally print the two names in order such that there is one space between them.
    """
    print( AUTHOR + exercise6.__doc__, flush=True )  # Leave this as the first line of the function.

    first_name = input("What's your first name:")
    last_name = input("What's your last name:")


######## Main Program ########
if __name__ == "__main__":
    main()
