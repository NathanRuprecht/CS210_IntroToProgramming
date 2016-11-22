import math
import random

for i in range(91):
    degrees = i * 4
    radians = (degrees * math.pi) / 180
    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)
    print(degrees, sine, cosine, tangent)
