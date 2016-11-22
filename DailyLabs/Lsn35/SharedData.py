# CS 210 - Introduction to Programming - Fall 2014
#
# Author: Maj. Caswell, Dr. Bower
#
# Documentation Statement: None.
#

from threading import Thread

""" This file contains a example of the difficult
    of sharing data between threads.
"""

from threading import Thread

MAX = 1000000

def main():
    """ Main program to run the demo. """
    print( "Counting to {}.".format( MAX ), flush=True )

    # In order to pass an integer value by reference, make a list with
    # a single value in it. If this is unclear, see the diagrams here:
    # http://interactivepython.org/runestone/static/thinkcspy/Lists/ObjectsandReferences.html
    counter = [ 0 ]

    # Count sequentially, in a single thread, producing the expected result of 0.
    print( "Counting sequentially, in a single thread ... ", end="", flush=True )
    increment( counter )
    decrement( counter )
    print( "counter = {}".format( counter[ 0 ] ), flush=True )

    # Count in parallel, using two threads. What is the expected result?
    print( "Counting in two parallel threads ... ", end="", flush=True )
    t1 = Thread( target=increment, args=( counter, ) )
    t2 = Thread( target=decrement, args=( counter, ) )

    # Start both threads and then wait for both to finish.
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print( "counter = {}".format( counter[ 0 ] ), flush=True )


def increment( counter ):
    for i in range( MAX ):
        counter[ 0 ] += 1

def decrement( counter ):
    for i in range( MAX ):
        counter[ 0 ] -= 1

def run_stopwatch( start_time, stop_event ):
    """ Runs a stopwatch loop showing the time elapsed at regular intervals. """
    while not stop_event.is_set():
        sleep( 0.05 )  # Accurate to about 1/20th of a second.
        print( "{:.2f}".format( time() - start_time ), flush=True )  # Show current running time.


######## Main program ########
if __name__ == "__main__":
    main()
