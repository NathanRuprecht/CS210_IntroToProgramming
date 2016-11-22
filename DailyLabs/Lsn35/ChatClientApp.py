# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains a simple stopwatch application created with Qt Designer. """

# Put all import statements a the top of the file.
from ChatClientGui import Ui_ChatClient
from PyQt4 import QtCore, QtGui
from threading import Thread, Event
from time import time, sleep
import sys


class ChatClientApp:
    """ Application class to instantiate and controls a StopwatchGui. """

    def __init__( self ):
        """ Initialize and show the gui. """

        # Create the main window in which our gui will display.
        self.main_window = QtGui.QMainWindow()

        # Create an instance of our gui and set it up in the main window.
        self.gui = Ui_ChatClient()
        self.gui.setupUi( self.main_window )

        # Set the connections between the gui components and this application.
        self.gui.menu_connect.triggered.connect( self.connect )
        self.gui.menu_disconnect.triggered.connect( self.disconnect )
        self.gui.menu_save.triggered.connect( self.save )
        self.gui.menu_exit.triggered.connect( self.closeEvent )

        # Have the main window's closeEvent method call this application's closeEvent
        # method instead so the user can be asked if they really want to quit.
        self.main_window.closeEvent = self.closeEvent

        # Show the main window containing our gui.
        self.main_window.show()

    def connect( self ):
        """ Connect to a chat server. """
        print( "Connect ...", flush=True )

    def disconnect( self ):
        """ Disconnect from a chat server. """
        print( "Disonnect ...", flush=True )

    def save( self ):
        """ Save the current contents of the chat transcript to a file. """
        print( "Save ...", flush=True )

    def exit( self ):
        """ Close any open sockets and exit the application. """
        print( "Exit ...", flush=True )

    def closeEvent( self, event ):
        """ Call the exit function to ensure all sockets are closed. """
        self.exit()


def main():
    """ Main program to launch the counter application. """

    # Create a QApplication to handle event processing for our gui.
    app = QtGui.QApplication( sys.argv )

    # Create an instance of our application.
    chat_client = ChatClientApp()

    # Start the application executing, exiting when it returns (i.e., the window is closed).
    sys.exit( app.exec_() )  # Note the underscore at the end of exec_().


######## Main program ########
if __name__ == "__main__":
    main()
