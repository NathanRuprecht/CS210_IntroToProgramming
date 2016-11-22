# CS 210 - Introduction to Programming - Fall 2014
#
# Author: Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains the quintessential threading example of showing the
    current time from separate threads at regular yet different intervals.
"""

from threading import Thread
from time import time, ctime, sleep


def main():
    """ Main program to run the demo. """

    # Create several threads, each showing the current time at different intervals.
    print( "Creating threads ...", flush=True )
    threads = [ Thread( target=show_time, args=( 1, time(), 10, 3 ) ),
                Thread( target=show_time, args=( 2, time(), 8, 2 ) ),
                Thread( target=show_time, args=( 3, time(), 12, 4 ) ) ]

    # Start the threads.
    print( "Starting threads ...", flush=True )
    for t in threads:
        t.start()
    print( "Threads started ...", flush=True )

    # Signal that the main() function should wait until all threads have completed.
    for t in threads:
        t.join()

    # Due to the join() calls above, this message shows when all threads complete.
    print( "Done.", flush=True )


def show_time( id, start_time, duration, interval ):
    """ Shows the time at given intervals for the specified duration. """

    # Get and display the current time before starting the loop.
    current_time = time()
    print( "Thread {}: {}".format( id, ctime( current_time ) ), flush=True )

    # Loop until the current time exceeds the expected duration.
    while current_time - start_time < duration:
        # Sleep, get the new time, and show it.
        sleep( interval )
        current_time = time()
        print( "Thread {}: {}".format( id, ctime( current_time ) ), flush=True )


######## Main program ########
if __name__ == "__main__":
    main()
