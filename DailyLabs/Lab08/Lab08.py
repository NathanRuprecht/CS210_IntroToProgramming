#
#C2C Nathan Ruprecht
#CS 210 - T1 - Dr. Bower
#
#Lab08
#

""" Implement a Python program that allows a user to enter a number and
then prints the sum of the all the even numbers from 1 to the number and
then prints the sum of all the odd numbers from 1 to the number. """


def main():

    #define global variables
    sum_even = 0
    sum_odd = 0

    #get input number to be used
    input_number = int(input("Give me a number:"))

    #sum of EVEN numbers from 1 to input_number
    even(input_number, sum_even)

    #sum of ODD number from 1 to input_number
    odd(input_number, sum_odd)




def even(number, sum_even):
    for i in range(2, number, 2):
        sum_even = sum_even + i
    print("The sum of all the even numbers between 1 and", number,
          "is", sum_even)
    print("")



def odd(number, sum_odd):
    for i in range(1, number, 2):
        sum_odd = sum_odd + i

    print("The sum of all the odd numbers between 1 and", number,
          "is", sum_odd)


#start program
main()
