# CS 210 - Introduction to Programming - Fall 2014
# Author: Lt Col Weingart
# Section: T6A, LtCol Weingart
# Documentation Statement: N/A

from Employee import Employee

class HourlyEmployee( Employee ):
    """ This class models an hourly wage earning employee and is a subclass of Employee. """
    MINIMUM_WAGE = 8.00  # https://www.colorado.gov/pacific/cdle/minimumwage

    def __init__( self, id = 0, name = "", emailAddress = "", hourlyWage = MINIMUM_WAGE ):
        """ This method instantiates a new hourly employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
          id - an integer ID for the employee
          name - first and last name of the employee as a string
          emailAddress - email address for the employee as a string
          hourlyWage - the amount in dollars per hour that the employee earns
        Returns:
          Reference to an hourly employee ojbect.
        Preconditions:
          None.
        Postconditions:
          A new hourly employee object is created."""
        # The following is the Python 3 preferred method of calling super.
        #   http://legacy.python.org/dev/peps/pep-3135/
        #   https://docs.python.org/3/library/functions.html#super
        super().__init__( id, name, emailAddress ) # Calls the Employee class __init__ method.
        self.setHourlyWage( hourlyWage )

    def getHourlyWage( self ):
        """ This method gets the value of hourlyWage.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of hourlyWage is returned.
        Preconditions:
          None.
        Postconditions:
          Value of hourlyWage is returned."""
        return self.hourlyWage

    def setHourlyWage( self, hourlyWage = MINIMUM_WAGE ):
        """ This method sets the value of hourlyWage.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          HourlyEmployee object exists.
        Postconditions:
          hourlyWage is set to value passed in."""
        # Ensure that a negative wage is not allowed
        if hourlyWage < 0.0:
            raise ValueError("Error - wage must be greater than zero")
        self.hourlyWage = hourlyWage

    def reportCompensation( self ):
        """ This method returns a string prepresentation of the hourly employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
           A string representation of employee object is returned.
        Preconditions:
          None.
        Postconditions:
          A string representation of hourly employee object is returned."""
        # note call to parent class method and use of super() function
        return super().reportCompensation() + "Hourly wage: {0}\n".format( self.hourlyWage ) 
    
    def calcYearlyCompensation( self ):
        """ This method calculates the annual salary of an hourly employee.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Annual salary of hourly employee is returned.
        Preconditions:
          None.
        Postconditions:
          Annual salary of hourly employee is returned."""
        # Forty hours per week at the hourly wage times
        # fifty weeks per year, assuming two weeks off.
        return 40 * self.hourlyWage * 50
