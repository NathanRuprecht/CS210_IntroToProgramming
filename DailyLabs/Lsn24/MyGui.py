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
import random
from PolygonGui import Ui_PolygonGui
from PyQt4 import QtCore, QtGui
import sys

# Constant definitions go here, starting with your name.
AUTHOR = "C2C Nathan Ruprecht"
MARGIN = 32


######## Class Definitions Go Below Here ########

class PolygonApp:
    """ Application class to instantiate and control a PolygonGui. """

    def __init__ (self):
        """ Initialize and show the gui. """

        #Create the main window in which our gui will display.
        self.main_window = QtGui.QWidget() #Or QMainWindow()
        
        #Create an instance of our gui and set it up in the main window.
        self.gui = Ui_PolygonGui()
        self.gui.setupUi (self.main_window)

        #Set the connections between the gui componetns and this application
        self.gui.Triangle_Btn.clicked.connect(self.create_triangle)
        self.gui.Square_Btn.clicked.connect (self.create_square)
        self.gui.Parellelogram.clicked.connect (self.create_parellelogram)

        #Set the drawing widget's paint method to use this application's paint method.
        self.gui.widget.paintEvent = self.paintEvent

        #Set the drawing widget's mouse press method to use this application's method.
        self.gui.widget.mousePressEvent = self.mousePressEvent
        
        #Create an empty polygon to be drawn each time the gui paints.
        self.polygon = QtGui.QPolygon()

        #Show the main window containing our gui.
        self.main_window.show()

    def paintEvent (self, q_paint_event):
        """ Called automatically whenever the drawing widget needs to repaint. """

        #Get a QPainter object that can paint on the drawing widget.
        painter = QtGui.QPainter (self.gui.widget)
        painter.setBrush (QtCore.Qt.blue)
        painter.setPen (QtCore.Qt.blue)
        painter.drawPolygon (self.polygon)

    def mousePressEvent (self, q_mouse_event):
        """ Called automatically whenever the drawing widget is clicked."""
        #Create a QPoint with the coordinates of the mouse click.
        click_point = QtCore.QPoint (q_mouse_event.x(), q_mouse_event.y() )

        #Find the point in the polygon closest to the click point.
        closest_i = 0 #Index of the closest point
        closest_d = distance (click_point, self.polygon.first())
        for i in range(1, self.polygon.count() ):
            d = distance (click_point, self.polygon.point( i ) )
            if( d < closest_d ):
                closest_d = d
                closest_i = i

        #If the "Replace closest point" radio button in checked
        if self.gui.Insert_Btn.isChecked():
            self.polygon.insert( closest_i, click_point)
        else:
            #Replace the closest point with the click point.
            self.polygon.replace( closest_i, click_point )

        #Tell the drawing widget to update so the changed polygon is actually drawn.
        self.gui.widget.update()

    def create_triangle (self):
        """ Create a triable polygon to be drawn on the drawing widget. """

        #Get the width and height of the drawing widget and create the polygon points.
        w = self.gui.widget.width() - 1
        h = self.gui.widget.height() - 1
        self.polygon.setPoints ([ MARGIN, h-MARGIN, w//2, MARGIN, w-MARGIN, h-MARGIN ])

        #Tell the drawing widget to update so the polygon is actually drawn.
        self.gui.widget.update()

    def create_square (self):
        """ Create a square polygon to be drawn on the drawing widget. """

        #Get the width and height of the drawing widget and create the polygon points
        w = self.gui.widget.width() - 1
        h = self.gui.widget.height() - 1
        x = w//2
        y = h//2
        s = min( x,y ) - MARGIN
        self.polygon.setPoints( [ x-s, y-s, x+s, y-s, x+s, y+s, x-s, y+s ] )

        #Tell the drawing widget to update so the polygon is actually drawn.
        self.gui.widget.update()

    def create_parellelogram (self):
        """ Create a square polygon to be drawn on the drawing widget. """

        #Get the width and height of the drawing widget and create the polygon points
        w = self.gui.widget.width() - 1
        h = self.gui.widget.height() - 1
        x = w//2
        y = h//2
        s = min( x,y ) - MARGIN
        self.polygon.setPoints( [ x, y-s, x+s, y-s, x, y+s, x-s, y+s ] )

        #Tell the drawing widget to update so the polygon is actually drawn.
        self.gui.widget.update()

######## Class Definitions Go Above Here ########



# Leave the main function in front of any other non-class functions.
def main():
    """ Main program to launch the polygon application """

    #Creat a QApplication to handle event processing for our gui.
    app = QtGui.QApplication( sys.argv )

    #Create an instance of our application
    poly_app = PolygonApp()

    #Start the application executing, exiting when it returns (i.e., the window is closed).
    sys.exit(app.exec_() ) #Note the underscore at the end of exec_()


######## Non-Class Function Definitions Go Below Here ########

def distance( p, q ):
    """ Calculate and return the distance between point p and q. """
    return ( ( p.x() - q.x()) ** 2 + (p.y() - q.y() ) ** 2 ) ** 0.5




######## Non-Class Function Definitions Go Above Here ########



######## Main program ########
# These two lines are always the last two lines in the file.
if __name__ == "__main__":
    main()
