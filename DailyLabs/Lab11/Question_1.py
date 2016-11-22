# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

def main():
    print(newtonSqrt(10))

def newtonSqrt(n):
 approx = 0.5 * n
 better = 0.5 * (approx - n/approx)
 while better != approx:
     approx = better
     better = 0.5 * (approx - n/approx)
     print(approx)
 
 return approx


if __name__ == "__main__":
    main()
