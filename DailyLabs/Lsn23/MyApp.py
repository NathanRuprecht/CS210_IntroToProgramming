# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains _INSERT_DESCRIPTION_HERE_. """

# Put all import statements a the top of the file.
from CounterGui import Ui_CounterGui
from PyQt4 import QtCore, QtGui
import sys

# Constant definitions go here, starting with your name.
AUTHOR = "C2C Nathan Ruprecht"



######## Class Definitions Go Below Here ########

class CounterApp:
    """Application class to instantiate and control a CounterGui."""
    
    def __init__(self):
        """Initialize and show the gui."""

        #Create the main window in which our gui will display.
        self.main_window = QtGui.QWidget() #Or QMainWindow()

        #Create an instance of our gui and set it up in the main window.
        self.gui = Ui_CounterGui()
        self.gui.setupUi(self.main_window)

        #Set the connections between the gui components and this application.
        self.gui.inc_btn.clicked.connect(self.increment)
        self.gui.dec_btn.clicked.connect(self.decrement)

        #Show the main window containing our gui.
        self.main_window.show()

    def increment(self):
        """Increment the counter in the gui"""
        self.gui.count_label.setText(str( int( self.gui.count_label.text() ) +1 ))

    def decrement(self):
        """Decrement the counter in the gui"""
        self.gui.count_label.setText(str( int( self.gui.count_label.text() ) -1 ))
        
            


######## Class Definitions Go Above Here ########



# Leave the main function in front of any other non-class functions.
def main():
    """ Main program to _INSERT_DESCRIPTION_HERE_. """

    #Create a QApplication to handle event processing for our gui.
    app = QtGui.QApplication( sys.argv )

    #Create an instance of our application
    counter = CounterApp()

    #Start the application executing, exiting when it returns (i.e., the window is closed)
    sys.exit( app.exec_() ) #Note the underscore at the end of exec_()



######## Non-Class Function Definitions Go Below Here ########





######## Non-Class Function Definitions Go Above Here ########



######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
