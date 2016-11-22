# CS 210 - Introduction to Programming - Fall 2014
#
# Author: Troy Weingart, Randy Bower, Brad Miller, David Ranum
#
# Section: T6A, LtCol Weingart
#
# Documentation Statement: This class is adapated from the Point class
# presented by Brad Miller and David Ranum in our online textbook.
#

""" This file contains an introduction to Classes and Objects using a Point class. """

# The keyword "class" begins a class definition and is followed by the name of the class.
# Note that naming convention says class names begin with an upper-case letter. (This is
# why other variable names and function names do NOT begin with an upper-csae letter ...
# if they do, most programmers will be confused as they will think it is a class!)
class Point:
    """ Point class for representing and manipulating (x,y) coordinates. """

    # Note that all of the code from here to the end of the class definition is indented.
    # The first non-indented code encountered will mark the end of the class.

    # Note the assignment to zero in the parameter list for init_x and init_y.
    # These are called default arguments and will be used if no arguments are
    # specified, as in the following:
    #     p = Point()  # Creates a new Point with init_x=0 and init_y=0.
    def __init__( self, init_x = 0, init_y = 0 ):
        """ Constructor method to create a new Point at the given coordinates,
            using default values of (0,0) if init_x and init_y are not specified.
        """
        # Assignment statements in a class constructor method serve
        # as the definitions of the object's attributes.
        self.x = init_x
        self.y = init_y

    # Note that all class methods have 'self' as the first formal parameter,
    # which serves as a reference to the object itself. When these methods
    # are called in a main program, this parameter is not specified by the
    # programmer but is automatically set by Python to refer to the object
    # on which the method was called.

    def get_x( self ):
        """ Accessor method to retrieve a Point object's x-coordinate. """
        return self.x

    def get_y( self ):
        """ Accessor method to retrieve a Point object's x-coordinate. """
        return self.y

    def distance_from_origin( self ):
        """ Calculate and return the distance from the origin to this point. """
        return ( self.x ** 2 + self.y ** 2 ) ** 0.5

    def distance_from_point( self, other ):
        """ Calculate and return the distance from the other point to this point. """
        return ( ( self.x - other.x ) ** 2 + ( self.y - other.y ) ** 2 ) ** 0.5

    def midpoint( self, other ):
        """ Create and return a new Point object that is the midpoint
            between this point and the other point.
        """
        return Point( ( self.x + other.x ) / 2, ( self.y + other.y ) / 2 )

    # Overriding the __str__ method determines how instances of this class
    # will print when passed to the print() function.
    # Note this method must return a string (not actually print anything!)
    def __str__( self ):
        """ Create and return a string representation of this Point object. """
        return "({0},{1})".format( self.x, self.y )

    # Overriding the __eq__() method allows the programmer to define what it
    # means for two Point objects to be equal. This method is called when
    # the == comparison operator is used between to Point objects.
    # By default, Python's definition of == does "shallow" equality.
    
    ## Block 3b
    #def __eq__( self, other ):
    #    """ Determine if this point is equal to the other point with equality
    #        requiring both the x and y coordinates to be equal.
    #        Returns True if the points are equal; False otherwise.
    #    """
    #    return self.x == other.x and self.y == other.y


def main():
    """ Main program to demonstrate and test the Point class. """
    
    print( "Lab 22, Exercise 2:\n" )
    
    ## Block 1
    """
    p = Point( 1, 1 )
    q = Point( 1, 1 )
    print( "p = ", p, ", q = ", q, sep="" )
    print( p == q )
    """

    ## Block 2
    """
    p = Point( 2, 2 )
    q = p
    print( "p = ", p, ", q = ", q, sep="" )
    p.x = 4
    p.y = 3
    print( "p = ", p, ", q = ", q, sep="" )
    print( p == q )
    print( p is q )
    """

    ## Block 3a (Be sure to un-comment Block 3b above as well!)
    """
    p = Point( 5, 7 )
    q = Point( 5, 7 )
    print( "p = ", p, ", q = ", q, sep="" )
    print( p == q )
    print( p is q )
    """



######## Main Program ########
if __name__ == "__main__":
    main()
