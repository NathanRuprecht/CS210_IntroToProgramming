# CS 210 - Introduction to Programming - Fall 2014
# Author: Lt Col Weingart
# Section: T6A, LtCol Weingart
# Documentation Statement: N/A

class Employee( object ):
    """ This class models an employee. """

    def __init__( self, id = 0, name = "", emailAddress = "" ):
        """ This method instantiates a new employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
          id - an integer ID for the employee
          name - first and last name of the employee as a string
          emailAddress - email address for the employee as a string
        Returns:
          Reference to employee ojbect.
        Preconditions:
          None.
        Postconditions:
          A new employee object is created."""
        self.employeeID = id
        self.employeeName = name
        self.employeeEmailAddress = emailAddress

    def getEmployeeID( self ):
        """ This method gets the value of employeeID.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of emplyeeID is returned.
        Preconditions:
          None.
        Postconditions:
          Value of emplyeeID is returned."""
        return self.employeeID

    def setEmployeeID( self, employeeID ):
        """ This method sets the value of employeeID.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          Employee object exists.
        Postconditions:
          employeeID is set to value passed in."""
        self.employeeID = employeeID;
    
    def getEmployeeName( self ):
        """ This method gets the value of employeeName.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of employeeName is returned.
        Preconditions:
          None.
        Postconditions:
          Value of employeeName is returned."""
        return self.employeeName

    def setEmployeeName( self, employeeName ):
        """ This method sets the value of employeeName.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          Employee object exists.
        Postconditions:
          employeeName is set to value passed in."""
        self.employeeName = employeeName

    def getEmployeeEmailAddress( self ):
        """ This method gets the value of employeeEmailAddress.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of employeeEmailAddress is returned.
        Preconditions:
          None.
        Postconditions:
          Value of employeeEmailAddress is returned."""
        return self.employeeEmailAddress

    def setEmployeeEmailAddress( self, employeeEmailAddress ):
        """ This method sets the value of employeeEmailAddress.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          Employee object exists.
        Postconditions:
          employeeEmailAddress is set to value passed in."""
        self.employeeEmailAddress = employeeEmailAddress

    def reportCompensation( self ):
        """ This method returns a string prepresentation of the employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
           A string representation of employee object is returned.
        Preconditions:
          None.
        Postconditions:
          A string representation of employee object is returned."""
        return "ID: {0}\nName: {1}\nEmail: {2}\n".format( self.employeeID, self.employeeName, self.employeeEmailAddress )
