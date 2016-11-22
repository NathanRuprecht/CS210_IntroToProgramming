# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: _YOUR_SECTION_HERE_, _YOUR_INSTRUCTOR_HERE_
#
# Documentation Statement: None.
#

""" This file contains examples of recursive functions. """

# Leave the main function in front of any other non-class functions.
def main():
    """ Main program to demonstrate recursive functions. """

    # Testing the factorial() function.
    print( "Factorial of 5 =", factorial( 5 ) )
    print( "Factorial of 5 =", factorial_verbose( 5 ) )
    print()

    # Testing the fibonacci() function.
    print( "The {}st Fibonacci number is {}.".format( 1, fibonacci( 1 ) ) )
    print( "The {}th Fibonacci number is {}.".format( 8, fibonacci( 8 ) ) )
    print( "The {}th Fibonacci number is {}.".format( 13, fibonacci( 13 ) ) )
    print()

    # Testing the gcd() function.
    print( "gcd:", gcd( 14, 35 ), gcd( 49, 21 ), gcd( 14, 21 ), gcd( 21, 14 ) )
    print( "gcd:", gcd( 19, 51 ), gcd( 51, 19 ) )
    print()

    # Testing the list_sum() function and first/rest helper functions.
    a_list = [ 37, 83, 42, 51, 99, 13, 29, 67 ]
    print( "a_list = ", a_list )
    print( "first = {}, rest = {}".format( first( a_list ), rest( a_list ) ) )
    print( "Sum of a_list =", list_sum( a_list ) )
    print( "Sum of a_list =", list_sum_verbose( a_list ) )
    print()

    # Testing the list_contains() function.
    print( "{} contains {}: {}".format( a_list, 42, list_contains( 42, a_list ) ) )
    print( "{} contains {}: {}".format( a_list, 13, list_contains( 13, a_list ) ) )
    print( "{} contains {}: {}".format( a_list, 37, list_contains( 37, a_list ) ) )
    print( "{} contains {}: {}".format( a_list, 67, list_contains( 67, a_list ) ) )
    print( "{} contains {}: {}".format( a_list, 50, list_contains( 50, a_list ) ) )
    print( "{} contains {}: {}".format( a_list, 19, list_contains( 19, a_list ) ) )
    print()

    # Testing the list_count() function. These tests start with a string and
    # use the list() function to create a list of individual characters.
    s = "This is a test. This is only a test."
    print( "'{}' contains {} {} times.".format( s, 'e', list_count( 'e', list( s.lower() ), 0) ) )
    print( "'{}' contains {} {} times.".format( s, 't', list_count( 't', list( s.lower() ), 0) ) )
    print( "'{}' contains {} {} times.".format( s, 'z', list_count( 'z', list( s.lower() ), 0) ) )
    print()

    # Testing the list_merge() function. These tests also start with strings,
    # use the list() function to create a list of individual characters,
    # and then the string join() function to show the result as a string.
    print( "".join( list_merge( list( "aeiou" ), list( "cfmsw" ) ) ) )
    print( "".join( list_merge( list( "abcghimnostuyz" ), list( "defjklpqrvwx" ) ) ) )
    print( "".join( list_merge( list( "abcd" ), list( "wxyz" ) ) ) )
    print( "".join( list_merge( list( "wxyz" ), list( "abcd" ) ) ) )
    print()

    # A list of strings, some palindromes, some not.
    palindromes = [ "Go hang a salami; I'm a lasagna hog.", "Able was I ere I saw Elba.",
                    "Madam, I'm Adam.", "Madam in Eden, I'm Adam", "Never odd or even",
                    "Lee has a race car as a heel.", "No sir! Away! A papaya war is on!",
                    "Stressed? No tips? Spit on desserts.", "Mr. Owl ate my metal worm.",
                    "Flee to me, remote Elf!", "So many Dynamos!", "1001001", "Huh?",
                    "This is not a palindrome.", "Neither is this." ]

    # Testing the is_palindrome() function.
    #for p in palindromes:
    #    print( p, is_palindrome( p ) )
    #print()

    # My favorite binary tree:
    #         42
    #     25      75
    #   13  37  67  88
    # My favorite tree stored as a nested list.
    a_tree = [ 42, [ 25, [ 13, [], [] ],
                         [ 37, [], [] ] ],
                   [ 75, [ 67, [], [] ],
                         [ 88, [], [] ] ] ]

    # Print an in-order traversal of a binary tree.
    #in_order( a_tree )
    #print()



def factorial( n ):
    """ Recursively calculates the factorial of a given number.
    Parameters:
        n: A non-negative integer value.
    Returns:
        The factorial of n.
    Preconditions:
        The parameter n must be a non-negative integer.
    Postconditions:
        None.
    Raises:
        TypeError if n is not an integer.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial( n - 1 )


def factorial_verbose( n ):
    """ Recursively calculates the factorial of a given number
        while also printing trace information.
    Parameters:
        n: A non-negative integer value.
    Returns:
        The factorial of n.
    Preconditions:
        The parameter n must be a non-negative integer.
    Postconditions:
        None.
    Raises:
        TypeError if n is not an integer.
    """
    print( "n = {}:".format( n ), end=" " )
    if n <= 1:
        print( "returning 1." )
        return 1
    else:
        print( "calculating result = {} * factorial( {} )".format( n, n-1 ) )
        result = n * factorial_verbose( n - 1 )
        print( "n = {}: returning {}".format( n, result ) )
        return result


def fibonacci( n ):
    """ Recursively determines the nth Fibonacci number.
    Parameters:
        n: A non-negative integer value.
    Returns:
        The nth Fibonacci number.
    Preconditions:
        The parameter n must be a non-negative integer.
    Postconditions:
        None.
    Raises:
        TypeError if n is not an integer.
    """
    if n <= 0:
        return 0
    if n <= 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result


def gcd( m, n ):
    """ Recursively calculates the greatest common divisor of the given values.
    Parameters:
        m: A non-negative integer value.
        n: A positive integer value.
    Returns:
        The greatest common divisor of m and n.
    Preconditions:
        The parameter n must be a positive integer value.
    Postconditions:
        None
    Raises:
        TypeError if either m or n is not an integer.
    """
    if n <= 0:
        return m
    else:
        result = gcd(n, m % n)
        return result


def first( a_list ):
    """ Returns the first item in a list.
    Parameters:
        a_list: The list of which the first item is desired.
    Returns:
        The first item in the list.
    Preconditions:
        The parameter a_list is a non-empty list.
    Postconditions:
        The parameter a_list is unchanged.
    Raises:
        IndexError if a_list is empty.
        TypeError if a_list is not a list.
    """
    return a_list[0]


def rest( a_list ):
    """ Returns a list containing all items in a list except the first.
    Parameters:
        a_list: the list of which the rest is desired.
    Returns:
        A list containing all items from a_list except the first.
    Preconditions:
        The parameter a_list is a non-empty list.
    Postconditions:
        The parameter a_list is unchanged.
    Raises:
        TypeError if a_list is not a list.
    """
    return a_list[ 1: ]


def list_sum( num_list ):
    """ Recursively calculate and return the sum of a list of numbers.
    Parameters:
        a_list: the list of numbers whose sum is to be calculated.
    Returns:
        The sum of the numbers in the list.
    Preconditions:
        The parameter a_list is a (possibly empty) list.
    Postconditions:
        The parameter a_list is unchanged.
    Raises:
        TypeError if a_list is not a list.
    """
    if not num_list:
        return 0
    else:
        return first( num_list ) + list_sum( rest( num_list ) )

def list_sum_verbose( num_list ):
    """ Recursively calculate and return the sum of a list of numbers
        while also printing trace information.
    Parameters:
        a_list: the list of numbers whose sum is to be calculated.
    Returns:
        The sum of the numbers in the list.
    Preconditions:
        The parameter a_list is a (possibly empty) list.
    Postconditions:
        The parameter a_list is unchanged.
    Raises:
        TypeError if a_list is not a list.
    """
    print( "num_list = {}:".format( num_list ), end=" " )
    if not num_list:
        print( "returning 0." )
        return 0
    else:
        print( "calculating result = {} + list_sum( {} )".format( first( num_list ), rest( num_list ) ) )
        result = first( num_list ) + list_sum_verbose( rest( num_list ) )
        print( "num_list = {}: returning {}".format( num_list, result ) )
        return result


def list_contains( item, a_list ):
    """ Recursively determines if the given item is in the given list.
    Parameters:
        item: An item to be searched for in the given list.
        a_list: The list of items to be searched.
    Returns:
        True if the item is in the list; False otherwise.
    Preconditions:
        The list parameter must be a list.
    Postconditions:
        The list parameter is unchanged.
    Raises:
        TypeError if a_list is not a list.
    """
    # The recursive algorithm to determine list membership is:
    # If the list is empty,
    # then the item is not in the list.
    # If the list is not empty and the item equals the first item in the list,
    # then the item is in the list.
    # If the list is not empty and the item does not equal the first item in the list,
    # the the item is in the list if it is in the rest of the list.
    if item == first(a_list):
        return True
    if len(a_list) >= 2:
        return list_contains(item, rest(a_list))
    else:
        return False


def list_count( item, a_list, total ):
    """ Recursively determines how many times the given item occurs in the given list.
    Parameters:
        item: An item to be searched for in the given list.
        a_list: The list of items to be searched.
    Returns:
        The number of times the item occurs in the list.
    Preconditions:
        The list parameter must be a list.
    Postconditions:
        The list parameter is unchanged.
    Raises:
        TypeError if a_list is not a list.
    """
    # The recursive algorithm to count item occurrences in a list is:
    # If the list is empty,
    # then the item occurs in the list zero times.
    # If the list is not empty and the item equals the first item in the list,
    # then the item occurs one plus the number of times in occurs in the rest of the list.
    # If the list is not empty and the item does not equal the first item in the list,
    # then the item occurs the number of times it occurs in the rest of the list.
    if item == first(a_list):
        total+=1
    if len(a_list) >= 2:
        return list_count(item, rest(a_list), total)
    return total


def list_merge( a_list, b_list ):
    """ Recursively merges the two sorted lists into one list.
    Parameters:
        a_list: A sorted list to be merged.
        b_list: A sorted list to be merged.
    Returns:
        A new list with the sorted contents of both a_list and b_list.
    Preconditions:
        Both parameters must be lists.
        Both lists must be sorted in ascending order.
    Postconditions:
        The list parameters are unchanged.
    Raises:
        TypeError if either a_list or b_list is not a list.
    """
    # The recursive algorithm to merge two sorted lists is:
    # If the first list is empty,
    # then the result is the second list.
    # If the second list is empty,
    # then the result is the first list.
    # If the first item in the first list is less than the first item in the second list,
    # then the result is a list containing the first item from the first list concatenated
    # with a the result of merging the rest of the first list with the second list.
    # If the first item in the second list is less than the first item in the first list,
    # then the result is a list containing the first item from the second list concatenated
    # with a the result of merging the rest of the second list with the first list.
    if len(a_list) == 0:
        return b_list
    if len(b_list) == 0:
        return a_list
    if a_list[0] <= b_list[0]:
        return a_list[0] + b_list[0]
    else:
        return b_list[0] + a_list[0]
    if len(a_list) >= 2:
        return list_merge(rest(a_list), rest(b_list))
    


def is_palindrome( s ):
    """ Recursively determines if the given string is a palindrome.
    Parameters:
        s: The string to be tested for palindrome-ness.
    Returns:
        True if the given string is a palindrome; False otherwise.
    Preconditions:
        The parameter s must be a string.
    Postconditions:
        None.
    Raises:
        TypeError if the parameter is not a string.
    """
    # See the lab document for a more detailed description of the recursive algorithm.
    return False


def in_order( tree ):
    """ Prints an in-order traversal of the given tree.
    Parameters:
        tree: A nested list representing a binary tree.
    Returns:
        None.
    Preconditions:
        The parameter must be a properly formed nested list
        representing a binary tree.
    Postconditions:
        The tree parameter is unchanged.
    Raises:
        TypeError if the parameter is not a properly formed nested list.
    """
    # This is a challenge exercuse; use the links in the reading
    # to find an implement the appropriate algorithm.
    pass


######## Main program ########
if __name__ == "__main__":
    main()
