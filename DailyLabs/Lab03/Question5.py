x = int(input("Input: "))
y = 0
z = 0

while x > 0:
	y = y + (x % 2) * 10 ** z
	z = z + 1
	x = x // 2
print(y)

##I set x = 10 like I did for the 'pen and paper' example.  I got the same
##answer so I called it a win!!!!
