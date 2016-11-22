# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

import socket
from threading import Thread

# This example uses a socket to communicate between separate programs
# running on the same machine (IP address 127.0.0.1; aka localhost).
HOST = '127.0.0.1'  # The localhost IP address.
PORT = 3742         # Arbitrary, non-privileged port.


def main():
    """ Main program to run the chat client transmitter. """
    print( "Chat client ...", flush=True )
    
    # Start the listener in a separate thread.
    t = Thread( target=listener )
    t.start()
    
    # Just call the transmitter and let it use the main thread.
    transmitter()


def listener():
    """ Main program to run the chat client transmitter. """
    print( "Chat Listener...", flush=True )

    # Use a try/finally construct to ensure the sockets are closed.
    try:
        # Create an INET, STREAMing socket, connect it to the server, and
        # send the "Listener" message to tell the server this is listening.
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.connect( ( HOST, PORT ) )
        sock.send( "Listening".encode() )

        # Listen indefinitely for messages from the server.
        message = ""  # Anything other than "shutdown" to get the loop started.
        while not "shutdown" in message.lower():
            message = sock.recv( 1024 ).decode()
            print( message, flush=True )

    finally:
        print( "Listener shutting down...", flush=True )
        sock.close()


def transmitter():
    """ Main program to run the chat client transmitter. """
    print( "Chat Transmitter...", flush=True )
    name = input( "Enter your name: " )

    # Use a try/finally construct to ensure the sockets are closed.
    try:
        # Send messages to the server indefinitely.
        s_message = ""  # Anything other than "bye" to get the loop started.
        while s_message.lower() != "bye":
            # Get a message to transmit (show a Python-like prompt).
            s_message = input( ">>> " )

            # Create an INET, STREAMing socket, connect it to the server,
            # and send the message (with a T prefix to indicate it is a
            # Transmission message) encoded as bytes.
            sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            sock.connect( ( HOST, PORT ) )
            sock.send( "T{} says: {}".format( name, s_message ).encode() )
            sock.close()

    finally:
        print( "Transmitter shutting down...", flush=True )
        sock.close()


######## Main program ########
if __name__ == "__main__":
    main()

    # Pause before closing the console window (remove this line if
    # your IDE automatically delays closing the console window).
    input( "Press enter to continue ..." )
