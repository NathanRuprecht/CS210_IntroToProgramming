import math
import random

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    addition = dice1 + dice2
    print(dice1, dice2, addition)
