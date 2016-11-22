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
from StopwatchGui import Ui_StopwatchGui
from PyQt4 import QtCore, QtGui
from threading import Thread, Event
from time import time, sleep
import sys


class StopwatchApp:
    """ Application class to instantiate and control a StopwatchGui. """

    def __init__( self ):
        """ Initialize and show the gui. """

        # Create the main window in which our gui will display.
        self.main_window = QtGui.QWidget()  # Or QMainWindow().

        # Create an instance of our gui and set it up in the main window.
        self.gui = Ui_StopwatchGui()
        self.gui.setupUi( self.main_window )

        # Set the connections between the gui components and this application.
        self.gui.start_stop_button.clicked.connect( self.start_stop )

        # Use an Event to communicate with the thread.
        self.stop_event = Event()  # Set to False by default; set to True
        self.stop_event.set()      # so stopwatch is not running at launch.

        # Show the main window containing our gui.
        self.main_window.show()

    def start_stop( self ):
        """ Start the stopwatch if it is not running; stop it if it is running. """
        if self.stop_event.is_set():
            # Stopwatch was stopped, so start it.
            self.stop_event.clear()
            self.timer_thread = Thread( target=self.run_stopwatch, args=( time(), ) )
            self.timer_thread.start()
        else:
            # Stopwatch was running, so stop it.
            self.stop_event.set()

    def run_stopwatch( self, start_time ):
        """ Runs a stopwatch loop showing the time elapsed at regular intervals. """
        self.start_time = start_time
        while not self.stop_event.is_set():
            sleep( 0.01 )  # Accurate to about 1/100th of a second.
            self.gui.time_label.setText( "{:.2f}".format( time() - self.start_time ) )


def main():
    """ Main program to launch the counter application. """

    # Create a QApplication to handle event processing for our gui.
    app = QtGui.QApplication( sys.argv )

    # Create an instance of our application.
    stopwatch = StopwatchApp()

    # Start the application executing, exiting when it returns (i.e., the window is closed).
    sys.exit( app.exec_() )  # Note the underscore at the end of exec_().


######## Main program ########
if __name__ == "__main__":
    main()
