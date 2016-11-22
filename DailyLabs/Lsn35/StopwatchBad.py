# CS 210 - Introduction to Programming - Fall 2014
#
# Author: Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains a BAD example of a stopwatch using a function.

Remember, this is a BAD example of a stopwatch that DOES NOT WORK. If
you run this program you will need to stop it manually, most likely by
pressing CTRL-C in the console window.

Line A waits for the user to press Enter and line B starts the stopwatch.
Lines C and D in the main() function would allow the user to press Enter
a second time to stop the stopwatch by setting the global stopped flag.

However, the code in the run_stopwatch() function has a loop that does not
terminate until the stopped flag is True (Line E), which cannot happen until
control returns to the main() function, which cannot happen until the loop
in the run_stopwatch() function terminates, which cannot happen until
control returns to the main() function, etc.

The solution is to use two threads, one to run the stopwatch and one to
wait for input from the user, as shown in the next example.
"""

from time import time, sleep

# Global variable to indicate when the stopwatch is stopped.
# (Remember, this is a BAD example!)
stopped = False


def main():
    """ Main program to run the BAD EXAMPLE of a simple stopwatch. """

    # Wait for the user to press Enter to start the stopwatch, then call the
    # run_stopwatch() function with the current time as the start time, and
    # then wait for the user press Enter again to stop the stopwatch, at which
    # point the variable stopped will be set to True to stop the stopwatch.
    ignore_the_input = input( "Press Enter to start the stopwatch..." )    # Line A
    run_stopwatch( time() )                                                # Line B
    ignore_the_input = input( "Press Enter to stop the stopwatch...\n" )   # Line C
    stopped = True  # Set the global variable to stop the stopwatch.       # Line D


def run_stopwatch( start_time ):
    """ Runs a stopwatch loop showing the time elapsed at regular intervals. """
    while not stopped:                                                     # Line E
        sleep( 0.05 )  # Accurate to about 1/20th of a second.
        print( time() - start_time, flush=True )  # Show current running time.


######## Main program ########
if __name__ == "__main__":
    main()
