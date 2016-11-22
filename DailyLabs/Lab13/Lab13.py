# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

def main():
    exercise1("ssssss", "sss")
    #exercise2()
    #exercise3()



def exercise1(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount += 1
    print (lettercount)


def exercise2():
    pass


def exercise3():
    pass



if __name__ == "__main__":
    main()
