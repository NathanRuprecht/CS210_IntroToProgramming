# CS 210 - Introduction to Programming - Fall 2014
# Author: Lt Col Weingart
# Section: T6A, LtCol Weingart
# Documentation Statement: N/A

from Employee import Employee
from HourlyEmployee import HourlyEmployee

class SalariedEmployee( Employee ):
    """ This class models an salaried employee and is a subclass of Employee. """
    # Minimum wage for 52 weeks at 40 hours per week;
    # i.e., two weeks of paid vacation over an hourly employee!
    BASE_SALARY = 52 * 40 * HourlyEmployee.MINIMUM_WAGE

    def __init__( self, id = 0, name = "", emailAddress = "", salary = BASE_SALARY ):
        """ This method instantiates a new salaried employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
          id - an integer ID for the employee
          name - first and last name of the employee as a string
          emailAddress - email address for the employee as a string
          salary - the amount in dollars per year that the employee earns
        Returns:
          Reference to an salaried employee ojbect.
        Preconditions:
          None.
        Postconditions:
          A new commissioned salaried object is created."""
        # The following is the Python 3 preferred method of calling super.
        #   http://legacy.python.org/dev/peps/pep-3135/
        #   https://docs.python.org/3/library/functions.html#super
        super().__init__( id, name, emailAddress )
        self.setSalary( salary )

    def getSalary( self ):
        """ This method gets the value of salary.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Value of salary is returned.
        Preconditions:
          None.
        Postconditions:
          Value of salary is returned."""
        return self.salary

    def setSalary( self, salary = BASE_SALARY ):
        """ This method sets the value of salary.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          None.
        Preconditions:
          SalariedEmployee object exists.
        Postconditions:
          salary is set to value passed in."""
        # Ensure that a negative commissionRate is not allowed
        if salary < 0.0:
            raise ValueError("Error - salary must be greater than zero")
        self.salary = salary

    def reportCompensation( self ):
        """ This method returns a string prepresentation of the salaried employee object.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
           A string representation of salaried employee object is returned.
        Preconditions:
          None.
        Postconditions:
          A string representation of salaried employee object is returned."""
        return super().reportCompensation() + "Salary: {0}\n".format( self.salary )

    def calcYearlyCompensation( self ):
        """ This method calculates the annual salary of an salaried employee.
        Parameters:
          self - The implicit reference to the object (required by Python).
        Returns:
          Annual salary of salaried employee is returned.
        Preconditions:
          None.
        Postconditions:
          Annual salary of salaried employee is returned."""
        return self.salary
