import socket

# This example uses a socket to communicate between separate programs
# running on the same machine (IP address 127.0.0.1; aka localhost).
HOST = '172.16.234.5'  # The localhost IP address.
PORT = 3742         # Arbitrary, non-privileged port.

def main():
    """ Main program to run the chat client transmitter. """
    print( "Chat Transmitter...", flush=True )

    # Use a try/finally construct to ensure the sockets are closed.
    try:
        # Send messages to the server indefinitely.
        while True:
            # Get a message to transmit (show a Python-like prompt).
            s_message = input( ">>> " )

            # Create an INET, STREAMing socket, connect it to the server,
            # and send the message (with a T prefix to indicate it is a
            # Transmission message) encoded as bytes.
            sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            sock.connect( ( HOST, PORT ) )
            sock.send( ( "T" + s_message ).encode() )
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
