# CS 210 - Introduction to Programming - Fall 2014
# Author: Lt Col Weingart
# Section: T6A, LtCol Weingart
# Documentation Statement: N/A

from HourlyEmployee import HourlyEmployee
from SalariedEmployee import SalariedEmployee
from CommissionedEmployee import CommissionedEmployee

def main():
    """ Reads employee information from a file and calculates the companies annual payroll """
    employees = readEmployeeData()
    print( "Total Salary: ${:0.2f}\n".format( calc_total( employees ) ) )
    for employee in employees:
        print( employee.reportCompensation() )


def calc_total( employees ):
    """ This method calculates the annual payroll for a company.
    Parameters:
      employees - a list of employee objects
    Returns:
      annual payroll for a company.
    Preconditions:
      None.
    Postconditions:
      Returns annual payroll for a company."""
    total = 0.0
    for employee in employees:
        total += employee.calcYearlyCompensation()
    return total


def readEmployeeData():
    """ This reads employee data from a file and returns a list of those objects.
    Parameters:
      None.
    Returns:
      Annual payroll for a company.
    Preconditions:
      None.
    Postconditions:
      Returns annual payroll for a company."""
    
    # create an empty list to hold Employee objects
    employees = []
    with open( "EmployeeData.txt" ) as data_file:
        for line in data_file:
            data = line.strip().split(':')

            # Based on the 4th column of data create an appropriate object and then add it to the list of objects.
            if data[3] == "hourly":
                employee = HourlyEmployee( int(data[0]), data[1], data[2], int(data[4]) )
            elif data[3] == "salaried":
                employee = SalariedEmployee(int(data[0]),data[1],data[2],int(data[4]) )
            else:
                employee = CommissionedEmployee( int(data[0]), data[1], data[2], int(data[4]), float(data[5]) )

            employees.append( employee )

    return employees


if __name__ == "__main__":
    main()
