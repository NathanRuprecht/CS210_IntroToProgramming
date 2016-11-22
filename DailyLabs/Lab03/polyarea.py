"""

So we're given the number of sides and the distance
from its midpoint perpendicular to an edge, the
apothem.

Take the apothem time tan(30) to get half the length
of one side.

The perimeter is equal to the number of sides times
2 times the number found above.

The area is the apothem times the perimeter, all
divided by 2

"""


import math

radius = int(input("Give me the distance from the midpoint to an edge:"))
number_of_sides = int(input("Give me the number of sides:"))

theta = 360 / (number_of_sides * 2)
O = radius * math.sin(theta)
A = radius * math.cos(theta)
perimeter = (O * 2) * number_of_sides
area = perimeter * A


print(area)
    
