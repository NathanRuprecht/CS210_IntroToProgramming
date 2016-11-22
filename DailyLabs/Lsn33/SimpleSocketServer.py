import socket
import base64
 
MSG_DATA = b'SGVsbG8gV29ybGQhICBZb3UgaGF2ZSByZWNlaXZlZCBhIG1lc3NhZ2Ugb3ZlciBhIHNvY2tldA=='
HOST = '127.0.0.1'    # Symbolic name meaning all available interfaces
PORT = 9231  # Arbitrary non-privileged port
 
class SocketServer():
    def __init__(self, bindHost = HOST, bindPort = PORT):
        """Create a generic socket for binding"""
        self.theSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            self.theSocket.bind((bindHost, bindPort))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + msg.strerror)
            exit()

        print('Socket bind complete; ready to send message')
 
    def listen(self):
        """Opens the socket for listening.  Once connected returns the connection stream for message transmission"""
        self.theSocket.listen(0)
        print('Socket now listening')
 
        #wait to accept a connection - blocking call
        self.conn, self.addr = self.theSocket.accept()

        print('Connected with ' + self.addr[0] + ':' + str(self.addr[1]))
        return self.conn

    def transmit(self, msg):
        """Transmits a message across the socket"""
        # send our message to the client
        self.conn.sendall(msg)
 
    def close(self):
        """Closes the socket and releases the port"""
        # close the connection and the socket
        self.conn.close()
        self.theSocket.close()

def main():
    print( "My IP address is", socket.gethostbyname(socket.gethostname()), flush=True )
    socketObj = SocketServer()
    socketObj.listen()
    socketObj.transmit(base64.b64decode(MSG_DATA))
    socketObj.close()

if __name__ == "__main__":
    main()
