import math

##i
print("i: pi is", math.pi)

##ii
variable = 180
radians = (variable * math.pi) / 180
print("ii:", variable, "converted to radians is", radians)

##iii
degrees = 180
radians = (degrees * math.pi) / 180
cosine = math.cos(radians)
print("iii: The cosine of", degrees, "is", cosine)

##iv
##stuff = fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
##print(stuff)

##v
a = 2
b = 3
first = a ** b
second = pow(a,b)
third = math.pow(a,b)
print("v: 3 ways to raise", a, "to the", b, "power:", first, second, third)

##vi
angle = 30
radians = (angle * math.pi) / 180
tangent = math.tan(radians)
other_tangent = (math.sin(radians)) / (math.cos(radians))
print("vi: The tan() of", angle, "degrees is", tangent,
      "while the sin()/cos()", "is", other_tangent)
