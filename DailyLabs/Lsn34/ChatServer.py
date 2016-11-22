import socket

# This example uses a socket to communicate between separate programs
# running on the same machine (IP address 127.0.0.1; aka localhost).
HOST = '127.0.0.1'  # The localhost IP address.
PORT = 3742         # Arbitrary, non-privileged port.

def main():
    """ Main program to run the chat server. """
    
    # Use a try/finally construct to ensure the sockets are closed.
    try:
        # Create an INET, STREAMing socket, bound to the host/port, ready to accept connections.
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.bind( ( HOST, PORT ) )
        sock.listen( 0 )
        print( "Chat server listening for connections...", flush=True )

        # An empty list to hold all of the ChatClientListeners.
        listeners = []

        # Let them sound their barbaric yawp over the rooftops infinitely.
        while True:
            # Accept a connection; this is a blocking call.
            conn, addr = sock.accept()

            # Get the message from the new conn socket (i.e., the connection socket).
            message = conn.recv( 1024 ).decode()
            print( message, flush=True )

            # Figure out what to do with the message/connection.
            if message[ 0 ] == "L":
                # This is a new listener, so save the connection and send a greeting.
                listeners.append( conn )
                conn.send( "Welcome to your local chat server where you'll hear everyone talk.".encode() )
            else:
                # This is a transmitter sending a message to the server,
                # so the server needs to send it to all listeners.
                for listener in listeners:
                    listener.send( message[ 1: ].encode() )  # Don't send the 'T' character.

                # Transmitters create a new socket each time, so close it.
                conn.close()

    finally:
        print( "Server shutting down...", flush=True )
        for listener in listeners:
            listener.close()
        sock.close()


######## Main program ########
if __name__ == "__main__":
    main()

    # Pause before closing the console window (remove this line if
    # your IDE automatically delays closing the console window).
    input( "Press enter to continue ..." )
