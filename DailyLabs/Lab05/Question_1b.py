import math
import random

##i
floating = random.random()
print("i:", floating)

##ii
integer = random.randint(10, 20)
print("ii:", integer)

##iii
more_floating = random.uniform(100, 200)
print("iii:", more_floating)

##iv
random.seed(a=9, version=2)
other = random.random()
print("iv:", other)
