# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

import math

def main():
    for angle in range(361):
        radians = math.radians(angle)
        print(angle, math.sin(radians), math.cos(radians), sep="\t")
        


if __name__ == "__main__":
    main()
