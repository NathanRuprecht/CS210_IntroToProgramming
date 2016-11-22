# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: This threading example is adapted from this example:
# https://www.daniweb.com/software-development/python/tutorials/238590/simple-threading-tutorial
#

""" This file contains a simple stopwatch using threads and a function. """

from threading import Thread, Event
from time import time, sleep


def main():
    """ Main program to run the simple stopwatch. """

    # An Event is a simple way to communicate with a thread. When the
    # run_stopwatch() function starts in the separate thread, the second
    # parameter is a _reference_ to the stop_event object. Thus, when
    # the main() thread calls stop_event.set(), it is the same Event
    # object in the stopwatch thread, so the thread will stop.
    stop_event = Event()

    # Wait for the user to start the stopwatch.
    ignore_the_input = input( "Press Enter to start the stopwatch..." )

    # Create and start a thread to run the stopwatch.
    t = Thread( target=run_stopwatch, args=( time(), stop_event, ) )
    t.start()

    # Wait for the user to stop the stopwatch.
    ignore_the_input = input( "Press Enter to stop the stopwatch...\n" )

    # This will signal the loop in run_stopwatch to stop.
    stop_event.set()


def run_stopwatch( start_time, stop_event ):
    """ Runs a stopwatch loop showing the time elapsed at regular intervals. """
    while not stop_event.is_set():
        sleep( 0.05 )  # Accurate to about 1/20th of a second.
        print( "{:.2f}".format( time() - start_time ), flush=True )  # Show current running time.


######## Main program ########
if __name__ == "__main__":
    main()
