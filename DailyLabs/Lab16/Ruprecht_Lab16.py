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

import random


def main():
    """ Main program to test solutions for each exercise. """
    #exercise1()
    #exercise2()
    #exercise3()
    #exercise4()
    #exercise5()
    exercise6()



######## Exercise 1 ########

def exercise1():
    """ Exercise 1 """
    print( AUTHOR + exercise1.__doc__, flush=True )  # Leave this as the first line of the function.

    a_list = [37, 83, 42, 51, 99, 13, 29, 67]
    print(len(a_list)) #a
    
    print(a_list[2]) #b
    
    print(a_list[7]) #c

    print(a_list[-1]) #c

    print(a_list[2:6]) #d

    e = a_list[3] #e
    a_list[3] = a_list[4]
    a_list[4] = e
    print(a_list)

    del a_list[3:5]#f
    print(a_list)

    b_list = a_list #g

    b_list.insert(3, 51)    #h it changed both lists since they're pointing
                            #at the same data
    b_list.insert(4, 99)
    print(a_list, b_list)

    a_list.sort() #i
    print(a_list, b_list)

    b_list = a_list[:] #j
    b_list.reverse()
    print(a_list, b_list)

    number = input("Number to check with list:") #k
    print(number in a_list)


######## Exercise 2 ########

def exercise2():
    """ Exercise 2 """
    print(  AUTHOR + exercise2.__doc__, flush=True )  # Leave this as the first line of the function.

    list_len = 9
    min_val = 10
    max_val = 99
    
    mylist = rand_list(list_len, min_val, max_val)
    print(mylist)

    mylist.sort()
    print(mylist)
    
    middle = list_len//2
    print(mylist[middle])

def rand_list(length, min, max):
    list = []
    for i in range(length):
        list.insert(i, random.randint(min, max))

    return list
        


######## Exercise 3 ########

def exercise3():
    """ Exercise 3 """
    print( AUTHOR + exercise3.__doc__, flush=True )  # Leave this as the first line of the function.

    list_len = 10
    min_val = 100
    max_val = 999
    
    mylist = rand_list(list_len, min_val, max_val)
    print(mylist)
    print(sum(mylist))
    add = 0
    for i in range(list_len):
        add += mylist[i]

    print(add)
    print(add/list_len)

######## Exercise 4 ########

def exercise4():
    """ Exercise 4 """
    print( AUTHOR + exercise4.__doc__, flush=True )  # Leave this as the first line of the function.

    list_len = 12
    min_val = 10
    max_val = 99

    mylist = rand_list(list_len, min_val, max_val)
    mylist.sort()
    print(mylist)
    del mylist[0:3]
    del mylist[6:11]
    mean = (sum(mylist))/list_len
    print("IQM = ", mean)


######## Exercise 5 ########

def exercise5():
    """ Exercise 5 """
    print( AUTHOR + exercise5.__doc__, flush=True )  # Leave this as the first line of the function.

    list_len = 6
    min_val = 1
    max_val = 42

    mylist = draw_lotto(list_len, min_val, max_val)
    print(mylist)

def draw_lotto(length, mini, maxi):
    mylist = []

    for i in range(length):
        mylist.insert(i, random.randint(mini, maxi))
    return mylist



######## Exercise 6 ########

def exercise6():
    """ Exercise 6 """
    print( AUTHOR + exercise6.__doc__, flush=True )  # Leave this as the first line of the function.

    list_len = 6
    min_val = 1
    max_val = 42
    count = 0

    winning_numbers = draw_lotto(list_len, min_val, max_val)
    mynumbers = draw_lotto(list_len, min_val, max_val)

    print(winning_numbers, mynumbers)
    for i in range(list_len):
        if winning_numbers[i] == mynumbers[i]:
            count +=1
    print(count, "numbers matched.")


######## Main Program ########
if __name__ == "__main__":
    main()
