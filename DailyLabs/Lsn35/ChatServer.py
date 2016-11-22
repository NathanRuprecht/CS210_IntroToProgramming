# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

import socket

# This example uses a socket to communicate between separate programs
# running on the same machine (IP address 127.0.0.1; aka localhost).
HOST = '127.0.0.1'  # The localhost IP address.
PORT = 3742         # Arbitrary, non-privileged port.

def main():
    """ Main program to run the chat server. """
    
    # Use a try/finally construct to ensure the sockets are closed.
    try:
        # The following line shows the IP address of the machine on which this code runs.
        # Use it to connect two machines rather than one machine through the locahost IP.
        #HOST = socket.gethostbyname( socket.gethostname() )
        #print( "My IP address is", HOST, flush=True )

        # Create an INET, STREAMing socket, bound to the host/port, ready to accept connections.
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.bind( ( HOST, PORT ) )
        sock.listen( 0 )
        print( "Chat server listening for connections...", flush=True )

        # Empty lists to hold all of the listeners and transmitters.
        listeners = []
        transmitters = [ "Server" ]  # One value to get the loop started.

        # Let them sound their barbaric yawp over the rooftops until they all bid adieu.
        while len( transmitters ) > 0:
            # Accept a connection; this is a blocking call.
            conn, addr = sock.accept()

            # Get the message from the new conn socket (i.e., the connection socket).
            message = conn.recv( 1024 ).decode()
            print( "Received '{}' from {}:{}.".format( message, addr[ 0 ], addr[ 1 ] ), flush=True )

            # Figure out what to do with the message/connection.
            if message[ 0 ] == "L":
                # This is a new listener, so save the connection and send a greeting.
                # Save both the conn and addr as a tuple.
                listeners.append( ( conn, addr ) )
                conn.send( "Welcome to your local chat server where you'll hear everyone talk.".encode() )
            else:
                # This is a transmitter sending a message to the server,
                # so the server needs to send it to all listeners.
                bad_listeners = []  # So we can remove listeners that have closed their connection.
                for listener in listeners:
                    try:
                        listener[ 0 ].send( message[ 1: ].encode() )  # Don't send the 'T' character.
                    except:
                        print( "Listener at {}:{} has left.".format( listener[ 1 ][ 0 ], listener[ 1 ][ 1 ] ), flush=True )
                        bad_listeners.append( listener )

                # Now remove the bad listeners and close their sockets.
                for bad_listener in bad_listeners:
                    bad_listener[ 0 ].close()
                    listeners.remove( bad_listener )

                # Transmitters create a new socket each time, so close it.
                conn.close()

                # If this is a new transmitter, save their name.
                name = message[ 1: message.find( ' ' ) ]
                if not name in transmitters:
                    transmitters.append( name )

                # If the message was "bye", remove this transmitter.
                if message.lower().endswith( "bye" ):
                    transmitters.remove( name )

                    # If this was the last transmitter, shut things down.
                    if len( transmitters ) == 1 and "Server" in transmitters:
                        # Removing "Server" will make the loop stop.
                        transmitters.remove( "Server" )
                        # Tell all the listners to shut down.
                        for listener in listeners:
                            listener[ 0 ].send( "shutdown".encode() )

    finally:
        print( "Server shutting down...", flush=True )
        for listener in listeners:
            listener[ 0 ].close()
        sock.close()


######## Main program ########
if __name__ == "__main__":
    main()

    # Pause before closing the console window (remove this line if
    # your IDE automatically delays closing the console window).
    input( "Press enter to continue ..." )
