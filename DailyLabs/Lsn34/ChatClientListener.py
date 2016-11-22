import socket

# This example uses a socket to communicate between separate programs
# running on the same machine (IP address 127.0.0.1; aka localhost).
HOST = '172.16.234.5'  # The localhost IP address.
PORT = 3742         # Arbitrary, non-privileged port.

def main():
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
        while True:
            message = sock.recv( 1024 ).decode()
            print( message, flush=True )

    finally:
        print( "Listener shutting down...", flush=True )
        sock.close()


######## Main program ########
if __name__ == "__main__":
    main()

    # Pause before closing the console window (remove this line if
    # your IDE automatically delays closing the console window).
    input( "Press enter to continue ..." )
