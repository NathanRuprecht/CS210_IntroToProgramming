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

O = radius * math.sin(30)
A = radius * math.cos(30)
tri = (O * A)
area = tri * number_of_sides


print(area)
    
