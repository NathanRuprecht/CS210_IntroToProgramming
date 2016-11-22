# CS 210 - Introduction to Programming - Fall 2014
# Author: Lt Col Weingart
# Section: T6A, LtCol Weingart
# Documentation Statement: N/A

from SalariedEmployee import SalariedEmployee

class CommissionedEmployee( SalariedEmployee ):
    """ This class models an salaried employee that also earns a commission and is a subclass of SalariedEmployee. """

    # Commission is above and beyond the base salary.
    BASE_COMMISSION = 0.10

    def __init__( self, id = 0, name = "", emailAddress = "", salary = SalariedEmployee.BASE_SALARY, commissionRate = BASE_COMMISSION ):
        """ This method instantiates a new commissioned employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
          id - an integer ID for the employee
          name - first and last name of the employee as a string
          emailAddress - email address for the employee as a string
          salary - the amount in dollars per year that the employee earns
          commissionrate - the amount a float that represents the percent commission per year
        Returns:
          Reference to an commissioned employee ojbect.
        Preconditions:
          commissionRate is a float > 0.0 and <= 1.0
        Postconditions:
          A new commissioned employee object is created."""
        # The following is the Python 3 preferred method of calling super.
        #   http://legacy.python.org/dev/peps/pep-3135/
        #   https://docs.python.org/3/library/functions.html#super
        super().__init__( id, name, emailAddress, salary )
        self.setCommissionRate( commissionRate )

    def getCommissionRate( self ):
        """ This method gets the value of hourlyWage.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of commissionRate is returned.
        Preconditions:
          None.
        Postconditions:
          Value of commissionRate is returned."""
        return self.commissionRate

    def setCommissionRate( self, commissionRate = BASE_COMMISSION ):
        """ This method sets the value of commissionRate.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          CommissionedEmployee object exists.
        Postconditions:
          commissionRate is set to value passed in."""
        # Ensure that a negative commissionRate is not allowed
        if commissionRate < 0.0:
            raise ValueError("Error - commission rate must be greater than zero")
        self.commissionRate = commissionRate

    def reportCompensation( self ):
        """ This method returns a string prepresentation of the commissioned employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
           A string representation of commissioned employee object is returned.
        Preconditions:
          None.
        Postconditions:
          A string representation of commissioned employee object is returned."""
        return super().reportCompensation() + "Commission rate: {:0.2%}\n".format( self.commissionRate )

    def calcYearlyCompensation( self ):
        """ This method calculates the annual salary of an commissioned employee.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Annual salary of commissioned employee is returned.
        Preconditions:
          None.
        Postconditions:
          Annual salary of commissioned employee is returned."""
        return self.salary + self.salary * self.commissionRate
