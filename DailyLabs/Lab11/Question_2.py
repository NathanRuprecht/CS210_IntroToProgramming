# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A, Dr. Bower
#
# Documentation Statement: None.
#

def main():
    list = [23, 12, 19, 32, 45, 56]
    length = len(list)
    
    for i in range(length):
        print("\n")
        for i in range(list[i]):
            print("*",end="")
        print(i+1)
        


if __name__ == "__main__":
    main()
